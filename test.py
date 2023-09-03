from elevenlabs import set_api_key, clone, generate, play
from dotenv import load_dotenv
import os 

load_dotenv()
ELEVEN_API_KEY = os.environ.get('ELEVEN_API_KEY')

set_api_key(ELEVEN_API_KEY)

voice = clone(
    name="mina",
    description="", # Optional
    files=["./sample_voice/01.wav", "./sample_voice/02.wav", "./sample_voice/03.wav", "./sample_voice/04.wav"],
)

test_text = "人工知能による日本語のテキストの生成及び日本語能力試験の難易度分析システムの開発に関する研究"
audio = generate(text=test_text, voice=voice)

play(audio)