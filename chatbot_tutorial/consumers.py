import asyncio
from channels.consumer import AsyncConsumer
import json
from channels.db import database_sync_to_async
from .views import respond_to_websockets
from chat_report.models import ChatJokesCounts, ChatCunsumerJokesCounts
from django.db.models import F

class ChatConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("connect")
        await self.send({
            "type" : "websocket.accept"
        })

    async def websocket_receive(self, event):
        text_data = event.get('text', None)
        if text_data is not None:
            load_data = json.loads(text_data)
            load_command = load_data.get('command')
            text = 'Hey! Just put on a smile'
            text = {
                "source": 'BOT',
                'type': 'text',
                'text': text,
            }

            if load_command == 'start':
                response = await self.start()
            elif load_command == 'send':
                response = await self.jokes(load_data)

            await self.send({
                "type": "websocket.send", 
                "text": json.dumps(response)
            })
    
    async def start(self):
        text = 'Hey! Just put on a smile'
        response = {
            "source": 'BOT',
            'type': 'text',
            'text': text,
        }
        return response

    async def jokes(self, load_data):
        response_data = {
            'text': load_data['joke_text'],
            'type': 'text',
            'source': 'CANDIDATE'
        }
        await self.send({
            "type": "websocket.send", 
            "text": json.dumps(response_data)
        })
        joke = load_data.get('text', None)
        if joke:
            await self.update_joke_count(joke)
            await self.update_consumer_joke_count(joke)

        user_name = self.scope['user']
        response = {
            "source": 'BOT',
        }
        result_message = respond_to_websockets(load_data)
        response.update(result_message)
        return response

    async def websocket_disconnect(self, event):
        await self.send({
            "type" : "websocket.close"
        })

    @database_sync_to_async
    def update_joke_count(self, joke):
        if ChatJokesCounts.objects.filter(joke=joke).exists():
            return ChatJokesCounts.objects.filter(joke=joke).update(count=F('count')+1)
        else:
            return ChatJokesCounts.objects.create(joke=joke,count=1)

    @database_sync_to_async
    def update_consumer_joke_count(self, joke):
        user = self.scope['user']
        if ChatCunsumerJokesCounts.objects.filter(user=user,joke=joke).exists():
            return ChatCunsumerJokesCounts.objects.filter(user=user,joke=joke).update(count=F('count')+1)
        else:
            return ChatCunsumerJokesCounts.objects.create(user=user,joke=joke,count=1)