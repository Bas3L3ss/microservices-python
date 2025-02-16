import pika,json

def upload(file, fs, channel, access):
    try:
        file_id = fs.put(file)
    except Exception as e:
        print(e)
        return 'Internal server error', 500
    
    message ={  
        "video_fid": str(file_id),
        "mp3_fid": None,
        "username": access["username"],
    }

    try:
        channel.basic_publish(exchange='', routing_key='video', body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),)
    except Exception as err:
        print(err)
        fs.delete(file_id)
        return "internal server error", 500

