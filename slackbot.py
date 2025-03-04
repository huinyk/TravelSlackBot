import os
import ssl
import certifi
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import slack_sdk
from dotenv import load_dotenv
from datetime import datetime
import logging

# 로깅 설정
logging.basicConfig(level=logging.DEBUG)

# .env 파일 로드
load_dotenv()

# 환경 변수 로드
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")

# SSL 설정
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Slack 클라이언트 생성
client = slack_sdk.WebClient(token=SLACK_BOT_TOKEN, ssl=ssl_context)

# Slack App 객체 생성 (한 번만)
app = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET,
    client=client,
    token_verification_enabled=False
)

#남은 시간 구하기
current_date = datetime.now() # 현재 날짜
target_date1 = datetime(2025, 11, 1) # 목표 날짜
days_left1 = (target_date1 - current_date).days # 남은 날짜 계산
target_date2 = datetime(2025, 5, 28)
days_left2 = (target_date2 - current_date).days
target_date3 = datetime(2025, 9, 19)
days_left3 = (target_date3 - current_date).days
target_date4 = datetime(2025, 4, 4)
days_left4 = (target_date4 - current_date).days


@app.event("app_mention")
def event_test(body, say, logger):
    logger.info(body)

    app.client.chat_postMessage(
        channel=body["event"]["channel"],  # 멘션이 발생한 채널에 메시지 전송
		  blocks=[
		{
			"type": "rich_text",
			"elements": [{"type": "rich_text_section","elements": [
						{"type": "text","text": "여행 D-day 봇", "style": {"bold": True}},
						{"type": "text","text": " "},
						{"type": "emoji","name": "형광봉01"},
						{"type": "text","text": "\n"}]},
				{
					"type": "rich_text_list",
					"style": "bullet",
					"indent": 0,
					"border": 0,
					"elements": [
												{
							"type": "rich_text_section",
							"elements": [
								{"type": "text","text": "훈님 도쿄까지 "},
								{"type": "text","text": f"{days_left4}일","style": {"code" : True}},
								{"type": "text","text": " 남았지롱"},
                {
									"type": "emoji",
									"name": "flag-jp",
									"unicode": "1f1ef-1f1f5"
								}
							]
						},
						{
							"type": "rich_text_section",
							"elements": [
								{"type": "text","text": "태훈님 포르투갈까지 "},
								{"type": "text","text": f"{days_left2}일","style": {"code" : True}},
								{"type": "text","text": " 남았지롱"},
                {
									"type": "emoji",
									"name": "flag-pt",
									"unicode": "1f1f5-1f1f9"
								}
							]
						},
						{
							"type": "rich_text_section",
							"elements": [
								{"type": "text","text": "보라님 호주까지 "},
								{"type": "text","text": f"{days_left3}일","style": {"code" : True}},
								{"type": "text","text": " 남았지롱"},
                {
									"type": "emoji",
									"name": "flag-au",
									"unicode": "1f1e6-1f1fa"
								}
							]
						},
						{
							"type": "rich_text_section",
							"elements": [
								{
									"type": "text",
									"text": "후슬님 이탈리아까지 "
								},
								{
									"type": "text",
									"text": f"{days_left1}일",
                  "style": {
                    "code" : True
                  }
								
								},
								{
									"type": "text",
									"text": " 남았지롱"
								},
                {
						    	"type": "emoji",
									"name": "it",
									"unicode": "1f1ee-1f1f9"
								}
							]
						}
					]
				}
			]
		}
	]
        
    )

if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()


