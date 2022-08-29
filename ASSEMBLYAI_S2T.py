from distutils.command.upload import upload

from numpy import save
import requests
#from api_secrets import API_KEY_ASSEMBLYAI
import sys
API_KEY_ASSEMBLYAI="aa66fa6ed0a74afaa43c7723a47fd191"
#upload
upload_endpoint='https://api.assemblyai.com/v2/upload'
trans_endpoint = "https://api.assemblyai.com/v2/transcript"
headers = {'authorization': API_KEY_ASSEMBLYAI}
filename="sample_long.wav"


def uploa(filename):
    def read_file(filename, chunk_size=5242880):
        with open(filename, 'rb') as _file:
            while True:
                data = _file.read(chunk_size)
                if not data:
                    break
                yield data

    
    response = requests.post(upload_endpoint,
                            headers=headers,
                            data=read_file(filename))
    audio_url = response.json()['upload_url']
    return audio_url

#transcribe
def transcribe(audio_url):
    json = { "audio_url": audio_url }

    response = requests.post(trans_endpoint, json=json, headers=headers)
    job_id=response.json()['id']
    return job_id
#poll
def poll(job_id):
    polling_endpoint=trans_endpoint+'/'+job_id
    poll_res=requests.get(polling_endpoint, headers=headers)
    return poll_res.json()
def get_trans_res_url(audio_url):
    trans_id=transcribe(audio_url)
    while True:
        data=poll(trans_id)
        if data['status']=='completed':
            return data,None
        elif data['status']=='error':
            return data,data["error"]


#save transcript
def save_trans(audio_url):
    data,error=get_trans_res_url(audio_url)
    
    if data:
        trans_filename= filename+".txt"
        with open(trans_filename,"w") as f:
            f.write(data['text'])
        print("Transcription saved")
    elif error:
        print("Error!!!",error)

audio_url=uploa(filename)
save_trans(audio_url)