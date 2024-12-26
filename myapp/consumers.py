from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
class MySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print("Websocket connect event",event)
        self.send({
            "type":"websocket.accept"
        })
        
    def websocket_receive(self,event):
        print("Websocket receive event",event)
        print('Message:',event['text'])
        
    def websocket_disconnect(self,event):
        print("Websocket disconnect event",event)
        raise StopConsumer()
        

class MyAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print("Websocket connect event",event)
        await self.send({
            "type":"websocket.accept"
        })
    
    async def websocket_receive(self,event):    
        print("Websocket receive event",event)
        print('Message:',event['text'])
        
    async def websocket_disconnect(self,event):
        print("Websocket disconnect event",event)
        raise StopConsumer()