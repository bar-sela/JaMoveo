import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from JaMoveo.models import CustomUser


class Consumer(WebsocketConsumer):
    def connect(self):
        self.user = self.scope["user"]
        self.user_id = self.user.id
        
        self.accept() #
        self.room_name = "rehearsal"
        async_to_sync(self.channel_layer.group_add)(
            self.room_name,
            self.channel_name)


    def receive(self, text_data):

        async_to_sync(self.channel_layer.group_send)(
            self.room_name, # שם הקקבוצה אלייה רוצים לשלוח את המילון
            {
                'type': 'global_handler',  #  This specifies the name of the method that should handle this message on the receiving end.
                'message': text_data ,
            }
        )

    def global_handler(self, event):
        # Send message to WebSocket for each channel
        data = json.loads(event['message']) # message key from the webSocket response
        if "Song" in data : # only if the message is a song info
            data['Song'] = {k: v for k, v in data.get('Song', {}).items() if k != 'photo'}
            if self.check_instrument_is_empty() :
                self.remove_chords_key( data['Song']['content'])
        self.send(text_data=json.dumps(data))

    def check_instrument_is_empty(self):
        return  CustomUser.objects.filter(id=self.user_id).values("instrument").first()["instrument"] == ""

    def remove_chords_key(self,song_data):
        for section in song_data:
            for item in section:
                if 'chords' in item:
                    del item['chords']

