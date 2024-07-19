import pika
import json

#upload file to mongodb using gridfs, put message in rabbitmq 
def upload(f, fs, channel, access):
    try:
        fid = fs.put(f)
    except Exception as err:
        print(err)
        return "internal server error - unable to upload video to mongodb", 500

    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access["username"],
    }
    
    try:
        channel.basic_publish(
            exchange="", 
            routing_key="video",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            )
        )
    except Exception as err:
        fs.delete(fid)
        print(err)
        return "internal server error - unable to publish video to queue", 500
