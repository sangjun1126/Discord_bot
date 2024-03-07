import discord
from datetime import datetime
from difflib import get_close_matches
 
# 토큰은 알아서 넣으셈 ㅇㅇ
 
class Champion :
    def __init__(self, name, description) :
        self.name = name
        self.description = description

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.champions = {
            '가렌': Champion('가렌', ''),
            '갈리오': Champion('갈리오', ''),
            '갱플랭크': Champion('갱플랭크', ''),
            '그라가스': Champion('그라가스', ''),
            '그레이브즈': Champion('그레이브즈', ''),
            '그웬': Champion('그웬', ''),
            '나르': Champion('나르', ''),
            '나미': Champion('나미', ''),
            '나서스': Champion('나서스', ''),
            '나피리': Champion('나피리', ''),
            '노틸러스': Champion('노틸러스', ''),
            '녹턴': Champion('녹턴', ''),
            '누누와 윌럼프': Champion('누누와 윌럼프', ''),
            '니달리': Champion('니달리', ''),
            '니코': Champion('니코', ''),
            '닐라': Champion('닐라', ''),
            '다리우스': Champion('다리우스', ''),
            '다이에나': Champion('다이에나', ''),
            '드레이븐': Champion('드레이븐', ''),
            '라이즈': Champion('라이즈', ''),
            '라칸': Champion('라칸', ''),
            '람머스': Champion('람머스', ''),
            '럭스': Champion('럭스', ''),
            '럼블': Champion('럼블', ''),
            '레나타': Champion('레나타', ''),
            '레넥톤': Champion('레넥톤', ''),
            '레오나': Champion('레오나', ''),
            '렉사이': Champion('렉사이', ''),
            '렐': Champion('렐', ''),
            '렝가': Champion('렝가', ''),
            '루시안': Champion('루시안', ''),
            '룰루': Champion('룰루', ''),
            '르블랑': Champion('르블랑', ''),
            '리 신': Champion('리 신', ''),
            '리븐': Champion('리븐', ''),
            '리산드라': Champion('리산드라', ''),
            '릴리아': Champion('릴리아', ''),
            '마스터 이': Champion('마스터 이', ''),
            '마오카이': Champion('마오카이', ''),
            '말자하': Champion('말자하', ''),
            '말파이트': Champion('말파이트', ''),
            '모데카이저': Champion('모데카이저', ''),
            '모르가나': Champion('모르가나', ''),
            '문도': Champion('문도', ''),
            '미스포츈': Champion('미스포츈', ''),
            '밀리오': Champion('밀리오', ''),
            '바드': Champion('바드', ''),
            '바루스': Champion('바루스', ''),
            '바이': Champion('바이', ''),
            '베이가': Champion('베이가', ''),
            '베인': Champion('베인', ''),
            '벡스': Champion('벡스', ''),
            '벨베스': Champion('벨베스', ''),
            '벨코즈': Champion('벨코즈', ''),
            '볼리베어': Champion('볼리베어', ''),
            '브라움': Champion('브라움', ''),
            '브라이어': Champion('브라이어', ''),
            '브랜드': Champion('브랜드', ''),
            '블라디미르': Champion('블라디미르', ''),
            '블리츠크랭크': Champion('블리츠크랭크', ''),
            '비에고': Champion('비에고', ''),
            '빅토르': Champion('빅토르', ''),
            '뽀삐': Champion('뽀삐', ''),
            '사미라': Champion('사미라', ''),
            '사이온': Champion('사이온', ''),
            '사일러스': Champion('사일러스', ''),
            '샤코': Champion('샤코', ''),
            '세나': Champion('세나', ''),
            '세라핀': Champion('세라핀', ''),
            '세주아니': Champion('세주아니', ''),
            '세트': Champion('세트', ''),
            '소나': Champion('소나', ''),
            '소라카': Champion('소라카', ''),
            '쉔': Champion('쉔', ''),
            '쉬바나': Champion('쉬바나', ''),
            '스몰더': Champion('스몰더', ''),
            '스웨인': Champion('스웨인', ''),
            '스카너': Champion('스카너', ''),
            '시비르': Champion('시비르', ''),
            '신짜오': Champion('신짜오', ''),
            '신드라': Champion('신드라', ''),
            '신지드': Champion('신지드', ''),
            '쓰레쉬': Champion('쓰레쉬', ''),
            '아리': Champion('아리', ''),
            '아무무': Champion('아무무', ''),
            '아우렐리온 솔': Champion('아우렐리온 솔', ''),
            '아이번': Champion('아이번', ''),
            '아지르': Champion('아지르', ''),
            '아칼리': Champion('아칼리', ''),
            '아크샨': Champion('아크샨', ''),
            '아트록스': Champion('아트록스', ''),
            '아펠리오스': Champion('아펠리오스', ''),
            '알리스타': Champion('알리스타', ''),
            '애니': Champion('애니', ''),
            '애니비아': Champion('애니비아', ''),
            '애쉬': Champion('애쉬', ''),
            '야스오': Champion('에코', ''),
            '에코': Champion('갈리오', ''),
            '엘리스': Champion('엘리스', ''),
            '오공': Champion('오공', ''),
            '오른': Champion('오른', ''),
            '오리아나': Champion('오리아나', ''),
            '올라프': Champion('올라프', ''),
            '요네': Champion('요네', ''),
            '요릭': Champion('요릭', ''),
            '우디르': Champion('우디르', ''),
            '우르곳': Champion('우르곳', ''),
            '워웍': Champion('워웍', ''),
            '유미': Champion('유미', ''),
            '이렐리아': Champion('이렐리아', ''),
            '이블린': Champion('이블린', ''),
            '이즈리얼': Champion('이즈리얼', ''),
            '일라오이': Champion('일라오이', ''),
            '자르반 4세': Champion('자르반', ''),
            '자야': Champion('자야', ''),
            '자이라': Champion('자이라', ''),
            '자크': Champion('자크', ''),
            '잔나': Champion('잔나', ''),
            '잭스': Champion('잭스', ''),
            '제드': Champion('제드', ''),
            '제라스': Champion('제라스', ''),
            '제리': Champion('제리', ''),
            '제이스': Champion('제이스', ''),
            '조이': Champion('조이', ''),
            '직스': Champion('직스', ''),
            '진': Champion('진', ''),
            '질리언': Champion('질리언', ''),
            '징크스': Champion('징크스', ''),
            '초가스': Champion('초가스', ''),
            '카르마': Champion('카르마', ''),
            '카밀': Champion('카밀', ''),
            '카사딘': Champion('카사딘', ''),
            '카서스': Champion('카서스', ''),
            '카시오페아': Champion('카시오페아', ''),
            '카이사': Champion('카이사', ''),
            '카직스': Champion('카직스', ''),
            '카타리나': Champion('카타리나', ''),
            '칼리스타': Champion('칼리스타', ''),
            '케넨': Champion('케넨', ''),
            '케이틀린': Champion('케이틀린', ''),
            '케인': Champion('케인', ''),
            '케일': Champion('케일', ''),
            '코그모': Champion('코그모', ''),
            '코르키': Champion('코르키', ''),
            '퀸': Champion('퀸', ''),
            '크산테': Champion('크산테', ''),
            '클레드': Champion('클레드', ''),
            '키아나': Champion('키아나', ''),
            '킨드레드': Champion('킨드레드', ''),
            '타릭': Champion('타릭', ''),
            '탈론': Champion('탈론', ''),
            '탈리아': Champion('탈리아', ''),
            '탐켄치': Champion('탐켄치', ''),
            '트런들': Champion('트런들', ''),
            '트리스타나': Champion('트리스타나', ''),
            '트린다미어': Champion('트린다미어', ''),
            '트위스티트 페이트': Champion('트위스티트 페이트', ''),
            '트위치': Champion('트위치', ''),
            '티모': Champion('티모', ''),
            '파이크': Champion('파이크', ''),
            '판테온': Champion('판테온', ''),
            '피들스틱': Champion('피들스틱', ''),
            '피오라': Champion('피오라', ''),
            '피즈': Champion('피즈', ''),
            '하이머딩거': Champion('하이머딩거', ''),
            '헤카림': Champion('헤카림', ''),
            '흐웨이': Champion('흐웨이', ''),
        }

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await self.change_presence(status=discord.Status.online, activity=discord.Game("대기"))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.lower().strip() == '예':
            await self.send_champion_info(message)
        elif message.content.lower().strip() == '아니오':
            await message.channel.send('좋아요. 다른 질문이 있으면 물어봐주세요!')
        else:
            answer = self.get_answer(message.content)
            await message.channel.send(answer)

    async def send_champion_info(self, message):
        # 예/아니오 버튼 전송
        embed = discord.Embed(title='가렌 정보', description='가렌에 대한 정보입니다.')
        embed.add_field(name='이름', value=self.champions['가렌'].name)
        embed.add_field(name='설명', value=self.champions['가렌'].description)
        msg = await message.channel.send(embed=embed)
        await msg.add_reaction('👍')  # 예 버튼
        await msg.add_reaction('👎')  # 아니오 버튼

    def get_day_of_week(self):
        weekday_list = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
        weekday = weekday_list[datetime.today().weekday()]
        date = datetime.today().strftime("%Y년 %m월 %d일")
        result = '{}({})'.format(date, weekday)
        return result

    def get_time(self):
        return datetime.today().strftime("%H시 %M분 %S초")

    def get_answer(self, text):
        trim_text = text.replace(" ", "")

        if trim_text == '' or None:
            return "알 수 없는 질문이에요. 답변을 드릴 수 없네요."
        elif trim_text in self.champions:
            return '{} 챔피언에 대한 꿀팁이에요. {}'.format(self.champions[trim_text].name, self.champions[trim_text].description)
        else:
            answer_dict = {
                '요일': ':calendar: 오늘은 {}입니다'.format(self.get_day_of_week()),
                '시간': ':clock9: 현재 시간은 {}입니다.'.format(self.get_time()),
            }
            
            for key in answer_dict.keys():
                if trim_text == key:
                    return answer_dict[key]

            # 가장 유사한 검색어 찾기
            matches = get_close_matches(trim_text, self.champions.keys(), n=1, cutoff=0.8)  # 유사도 임계값을 0.8로 설정
            if matches:
                return '유사한 단어를 찾았습니다: "{}". 이에 대한 정보를 보시겠습니까? (예/아니오)'.format(matches[0])
            else:
                return "해당하는 정보가 없습니다. 다른 질문을 해주세요."

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)
