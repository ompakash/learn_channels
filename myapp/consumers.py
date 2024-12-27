from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
from asgiref.sync import async_to_sync
import asyncio
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("Websocket connect event",event)
        # print("Channel layer:",self.channel_layer)
        print("Channel name:",self.channel_name)
        async_to_sync(self.channel_layer.group_add)("programmers",self.channel_name)
        self.send({
            "type":"websocket.accept"
        })
        
    def websocket_receive(self,event):
        # print("Websocket receive event",event)
        print('Message:',event['text'])
        async_to_sync(self.channel_layer.group_send)("programmers",{
            "type":"chat.message",
            "message":event['text']
        }) 
        
    def chat_message(self,event):
        print('event:',event)
        self.send({
            "type":"websocket.send",
            "text":event['message']
        })
        
        
    def websocket_disconnect(self,event):
        print("Websocket disconnect event",event)
        print("Channel layer:",self.channel_layer)
        print("Channel name:",self.channel_name)
        async_to_sync(self.channel_layer.group_discard)("programmers",self.channel_name)
        raise StopConsumer()
        

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print("Websocket connect event",event)
        await self.channel_layer.group_add("programmers",self.channel_name)
        await self.send({
            "type":"websocket.accept"
        })
    
    async def websocket_receive(self,event):    
        print("Websocket receive event",event)
        print('Message:',event['text'])
        await self.channel_layer.group_send("programmers",{
            "type":"chat.message",
            "message":event['text']
        })
         
    async def chat_message(self,event):
        print('event:',event)
        await self.send({
            "type":"websocket.send",
            "text":event['message']
        })
        
        
    async def websocket_disconnect(self,event):
        print("Websocket disconnect event",event)
        print("Channel layer:",self.channel_layer)
        print("Channel name:",self.channel_name)
        await self.channel_layer.group_discard("programmers",self.channel_name)
        raise StopConsumer()