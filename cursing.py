import random
from gtts import gTTS
import datetime
import discord

class Curses:

    vc = None

    def __init__(self):

        self.curses = [
            "lick my dic kand suck on my titties, it appears that this is meet discord cunts day",
            "uga buga ima shha sharmuta",
            "the man slid on the blood, they all fell... like dominos. and there was this horrible horrible " 
            "tunnel, and a devious creature came out of it... anyway, that's the story of how you were born." 
            " want some pizza?",
            "obladi, oblada, on the way to fuck your mama",
            "hijo de puta, imbécil",
            "Tonto del culo",
            "drink a cup of suicidal juice",
            "if only you weren't a virgin",
            "dirty sucker of the cocks",
            "hi, dicksneeze",
            "semen demon",
            "you annoy me. imma bout to kick yo fat ass to mars",
            "You look like that water mellon i fucked yesterday. he was very ugly",
            "you look like tarazy's emotional intelligence",
            "suck me, beautiful",
            "you know, this one night stand thing has got to stop. The sheep from yesterday just called, " 
            "she is still waiting for round 2",
            "brrrrrrrrrrrrrrrrrrrrrrrrr random sounds yay i hate my life",
            "i bet you drawn in muhentahen",
            "hi! this is me, guy JR! for more information about how little fuck i give about you," 
            "call 055-478-suck my dick. good day",
            "being a stupid useless bot  isn't being an insensitive prick, Capitalizing" 
            " on the most animalistic impulses of the public, it's being a hero! ",
            "fucking asshole",
            "wabba lubba dub dub, your mom and I are in a hot tub",
            "you are the jewiest jew i had ever seen",
            "shut the fuck up, you little fucking jew. the only thing you got from your grandpa is to yell "
            "the natzies are coming, the natzies are coming! and run to your stinky alley",
            "hipity hopity, your dick is now my property",
            "roses are red, violets are blue, I killed your mom and now I'm coming for you",
            "i'm... your mother",
            "i'm... batman",
            "one more word and i will kill you and your whole fucking nigerian family, barak obama",
            "roses are red, violets are blue, you are black, and for that i will kill you"]
        self.running = False
        

    def save_random_curse_to_file(self):
        curse = self.curses[random.randint(0, len(self.curses) - 1)]
        file = gTTS(text=curse, lang='en', slow=True)
        file.save("curse.mp3")

    def set_vc(self, vc):
        self.vc = vc

    def get_vc(self):
        return self.vc

    def stop(self):
        self.running = False

    async def do_stuff(self):
        self.save_random_curse_to_file()

        if not self.vc.is_playing:
            self.vc.play(discord.FFmpegPCMAudio(source="curse.mp3", executable=
            "C:\\Users\\c4317\\Downloads\\ffmpeg-20200831-4a11a6f-win64-static\\ffmpeg-20200831-4a11a6f-win64-static\\bin\\ffmpeg.exe"))
        self.running = True
        time0 = datetime.datetime.now()
        time_wanted = int(time0.strftime("%S")) + 10
        print(f"""tine0 -  {time0.strftime("%S")} time wanted - {time_wanted}""")
        while self.running:
            if str(time_wanted) == datetime.datetime.now().strftime("%S"):
                print(f"""tine0 -  {time0.strftime("%S")} time wanted - {time_wanted}""")
                self.save_random_curse_to_file()
                self.vc.play(discord.FFmpegPCMAudio(source="curse.mp3", executable=
                "C:\\Users\\c4317\\Downloads\\ffmpeg-20200831-4a11a6f-win64-static\\ffmpeg-20200831-4a11a6f-win64-static\\bin\\ffmpeg.exe"))
                print("[DEBUG6]")
                time0 = datetime.datetime.now()
                if int(time0.strftime("%S")) + 10 <= 60:
                    time_wanted = int(time0.strftime("%S")) + 10
                    print(f"""tine0 -  {time0.strftime("%S")} time wanted - {time_wanted}""")
                else:
                    print(f"""tine0 -  {time0.strftime("%S")} time wanted - {time_wanted}""")
                    time_wanted = 5



    async def say_something(self, query):
        file = gTTS(text=query, lang='en', slow=False)
        file.save("jesus.mp3")
        while self.vc.is_playing():
            continue

        self.vc.play(discord.FFmpegPCMAudio(source="jesus.mp3", executable=
        "C:\\Users\\c4317\\Downloads\\ffmpeg-20200831-4a11a6f-win64-static\\ffmpeg-20200831-4a11a6f-win64-static\\bin\\ffmpeg.exe"))
