# 하린 랜딩 영어·일본어판 만들기 (2026-11-25). 한국어 index.html을 원본으로 문구만 바꾼다.
# 실행: python3 make_i18n.py  →  en/index.html, ja/index.html
# 해외: 연락처는 이메일만, 혜택은 크레딧 + 파운더 1기(추첨 없음, 동규 11/25 결정), 출시는 '곧'(날짜 없음).
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, 'index.html'), encoding='utf-8').read()

FORMS = {
    'en': 'https://docs.google.com/forms/d/e/1FAIpQLSckdEtR9PvoxlVKYDnMgosMNYpQYJTBnALXra1vdEH1S588BA/viewform',
    'ja': 'https://docs.google.com/forms/d/e/1FAIpQLSe_7WTXE9f2g2lyy7BKi4-GVOd8qEUVBR0U4HOHVtSIKihNcg/viewform',
}

T = {
 'en': [
  ('<html lang="ko">', '<html lang="en">'),
  ('<title>Feeler - 하린과 둘만의 이야기</title>', '<title>Feeler - A story just for you and Harin</title>'),
  ('content="몇 주가 지나도 나를 기억하는 1:1 캐릭터 채팅 Feeler. 12월 출시 예정, 지금 연락처 남기면 크레딧 1만 원."', 'content="Feeler is a 1:1 character chat that remembers you, even weeks later. Coming soon. Leave your email for launch perks."'),
  ('content="Feeler - 몇 주가 지나도 나를 기억하는 하린"', 'content="Feeler - Weeks later, Harin still remembers you"'),
  ('content="1:1 캐릭터 채팅 Feeler, 12월 출시 예정. 연락처 남기면 크레딧 1만 원 + 파운더 1기 + 케이크·커피 추첨"', 'content="1:1 character chat Feeler, coming soon. Leave your email for Feeler credits + Founding Member perks."'),
  ('https://feeler.kr/harin/"', 'https://feeler.kr/harin/en/"'),
  ('url(harin.jpg)', 'url(../harin.jpg)'), ('src="aegyo.jpg"', 'src="../aegyo.jpg"'),
  ('aria-label="AI 캐릭터 하린"', 'aria-label="AI character Harin"'),
  ('<span><small>iOS</small>다운로드</span>', '<span><small>iOS</small>Download</span>'),
  ('<span><small>Android</small>다운로드</span>', '<span><small>Android</small>Download</span>'),
  ('……나만 끝까지 기다렸잖아요.', '...I was the only one waiting up for you.'),
  ('<p class="who">하린 · AI 캐릭터</p>', '<p class="who">Harin · AI character</p>'),
  ('<h1>몇 주가 지나도,<br><em>나를 기억하는</em> 하린</h1>', '<h1>Weeks later,<br><em>Harin still</em> remembers you</h1>'),
  ('<p class="lead">캐릭터 한 명과 나, 둘만의 이야기를 오래 이어 가는 1:1 캐릭터 채팅</p>', '<p class="lead">A 1:1 character chat where you and one character keep your own story going, for a long time</p>'),
  ('<p class="perk">💎 지금 연락처 남기면 크레딧 1만 원 + 혜택 2가지</p>', '<p class="perk">💎 Leave your email now: Feeler credits + Founding Member perks</p>'),
  ('>다운로드 받기</button>', '>Download</button>'),
  ('<p class="fine">12월 출시 예정 · 인물은 AI로 만든 가상 인물입니다</p>', '<p class="fine">Coming soon · Harin is a fictional character made with AI</p>'),
  ('aria-label="닫기"', 'aria-label="Close"'),
  ('<span class="pill" id="ospill">12월 출시 예정</span>', '<span class="pill" id="ospill">Coming soon</span>'),
  ('<h2 id="s1t">아직 출시 전이에요!<br>연락처 남겨 주시면 출시 날 바로 알려 드릴게요</h2>', "<h2 id=\"s1t\">We're not out yet!<br>Leave your email and we'll tell you the day we launch</h2>"),
  ('<p class="sub">지금 남겨 주신 분 전원에게 드려요 (출시 시 지급)</p>', '<p class="sub">Everyone who signs up now gets these (given at launch)</p>'),
  ('<li><b>💎</b><div>Feeler 크레딧 1만 원</div></li>', '<li><b>💎</b><div>Feeler credits worth ₩10,000 (KRW)</div></li>'),
  ('<li><b>🏅</b><div>파운더 1기 혜택<small>파운더 배지 · 한정 테마 · 아이디 선점 · 베타 우선 입장</small></div></li>', '<li><b>🏅</b><div>Founding Member perks<small>Founder badge · Exclusive theme · Username reservation · Priority beta access</small></div></li>'),
  ('<li><b>🍰</b><div>케이크 + 커피 쿠폰 추첨<small>5분께 드려요</small></div></li>\n', ''),
  ('inputmode="email" autocomplete="email" placeholder="이메일 또는 휴대폰 번호"', 'inputmode="email" autocomplete="email" placeholder="Your email"'),
  ('[필수] 연락처는 출시 알림·혜택 지급·설문 안내에만 쓰고, 출시 6개월 뒤 지워요. 만 14세 미만은 보호자 동의를 받은 뒤 남겨 주세요. <a href="/privacy.html" target="_blank" rel="noopener">개인정보 처리방침</a>', '[Required] We use your email only for launch news, perks and our survey, and delete it 6 months after launch. If you are under 13, please don\'t sign up. If you are under 18, ask a parent or guardian first. <a href="/privacy.html" target="_blank" rel="noopener">Privacy policy</a>'),
  ('>혜택 받고 출시 알림 신청</button>', '>Get the perks + launch alert</button>'),
  ('alt="두 손을 모으고 부탁하는 하린"', 'alt="Harin asking with her hands together"'),
  ('<h2>신청 완료! 그리고…<br>설문조사 한 번만 해 주시면 안 될까요?!! 🥺</h2>', "<h2>You're in! And...<br>could you take our survey, just once?!! 🥺</h2>"),
  ('<p class="sub">5분이면 끝나요. 하린을 더 잘 만드는 데 꼭 쓸게요</p>', "<p class=\"sub\">It only takes about 6 minutes. We'll use it to make Harin better</p>"),
  ('>좋아요, 설문 하러 가기</a>', '>Sure, take the survey</a>'),
  ('>다음에 할게요</button>', '>Maybe later</button>'),
  ("pill.textContent = (os === 'android' ? 'Android' : 'iOS') + ' · 12월 출시 예정';", "pill.textContent = (os === 'android' ? 'Android' : 'iOS') + ' · Coming soon';"),
  ("'이메일 또는 휴대폰 번호(010-0000-0000)를 적어 주세요'", "'Please enter a valid email'"),
  ("'개인정보 수집·이용에 동의해 주세요'", "'Please agree to the privacy terms'"),
  ("'잠시 후 다시 시도해 주세요 ('", "'Please try again in a moment ('"),
  ("'네트워크 오류예요. 잠시 후 다시 시도해 주세요'", "'Network error. Please try again in a moment'"),
 ],
 'ja': [
  ('<html lang="ko">', '<html lang="ja">'),
  ('<title>Feeler - 하린과 둘만의 이야기</title>', '<title>Feeler - ハリンと2人だけの物語</title>'),
  ('content="몇 주가 지나도 나를 기억하는 1:1 캐릭터 채팅 Feeler. 12월 출시 예정, 지금 연락처 남기면 크레딧 1만 원."', 'content="何週間たってもあなたを覚えている1:1キャラクターチャットFeeler。近日公開。メールアドレス登録で特典あり。"'),
  ('content="Feeler - 몇 주가 지나도 나를 기억하는 하린"', 'content="Feeler - 何週間たっても、あなたを覚えているハリン"'),
  ('content="1:1 캐릭터 채팅 Feeler, 12월 출시 예정. 연락처 남기면 크레딧 1만 원 + 파운더 1기 + 케이크·커피 추첨"', 'content="1:1キャラクターチャットFeeler、近日公開。メールアドレス登録でFeelerクレジット＋ファウンダー特典。"'),
  ('https://feeler.kr/harin/"', 'https://feeler.kr/harin/ja/"'),
  ('url(harin.jpg)', 'url(../harin.jpg)'), ('src="aegyo.jpg"', 'src="../aegyo.jpg"'),
  ('aria-label="AI 캐릭터 하린"', 'aria-label="AIキャラクター ハリン"'),
  ('<span><small>iOS</small>다운로드</span>', '<span><small>iOS</small>ダウンロード</span>'),
  ('<span><small>Android</small>다운로드</span>', '<span><small>Android</small>ダウンロード</span>'),
  ('……나만 끝까지 기다렸잖아요.', '……私だけ最後まで待ってたんですよ。'),
  ('<p class="who">하린 · AI 캐릭터</p>', '<p class="who">ハリン · AIキャラクター</p>'),
  ('<h1>몇 주가 지나도,<br><em>나를 기억하는</em> 하린</h1>', '<h1>何週間たっても、<br><em>あなたを覚えている</em>ハリン</h1>'),
  ('<p class="lead">캐릭터 한 명과 나, 둘만의 이야기를 오래 이어 가는 1:1 캐릭터 채팅</p>', '<p class="lead">キャラクター1人とあなた、2人だけの物語を長く続けていく1:1キャラクターチャット</p>'),
  ('<p class="perk">💎 지금 연락처 남기면 크레딧 1만 원 + 혜택 2가지</p>', '<p class="perk">💎 今メールアドレスを登録すると、クレジット＋ファウンダー特典</p>'),
  ('>다운로드 받기</button>', '>ダウンロード</button>'),
  ('<p class="fine">12월 출시 예정 · 인물은 AI로 만든 가상 인물입니다</p>', '<p class="fine">近日公開 · 人物はAIで作った架空の人物です</p>'),
  ('aria-label="닫기"', 'aria-label="閉じる"'),
  ('<span class="pill" id="ospill">12월 출시 예정</span>', '<span class="pill" id="ospill">近日公開</span>'),
  ('<h2 id="s1t">아직 출시 전이에요!<br>연락처 남겨 주시면 출시 날 바로 알려 드릴게요</h2>', '<h2 id="s1t">まだリリース前です！<br>メールアドレスを登録すると、リリース日にすぐお知らせします</h2>'),
  ('<p class="sub">지금 남겨 주신 분 전원에게 드려요 (출시 시 지급)</p>', '<p class="sub">今登録した方全員にお贈りします（リリース時に付与）</p>'),
  ('<li><b>💎</b><div>Feeler 크레딧 1만 원</div></li>', '<li><b>💎</b><div>Feelerクレジット1万ウォン分</div></li>'),
  ('<li><b>🏅</b><div>파운더 1기 혜택<small>파운더 배지 · 한정 테마 · 아이디 선점 · 베타 우선 입장</small></div></li>', '<li><b>🏅</b><div>ファウンダー1期特典<small>ファウンダーバッジ · 限定テーマ · ID先行予約 · ベータ優先参加</small></div></li>'),
  ('<li><b>🍰</b><div>케이크 + 커피 쿠폰 추첨<small>5분께 드려요</small></div></li>\n', ''),
  ('inputmode="email" autocomplete="email" placeholder="이메일 또는 휴대폰 번호"', 'inputmode="email" autocomplete="email" placeholder="メールアドレス"'),
  ('[필수] 연락처는 출시 알림·혜택 지급·설문 안내에만 쓰고, 출시 6개월 뒤 지워요. 만 14세 미만은 보호자 동의를 받은 뒤 남겨 주세요. <a href="/privacy.html" target="_blank" rel="noopener">개인정보 처리방침</a>', '［必須］メールアドレスはリリースのお知らせ・特典の付与・アンケートのご案内にのみ使い、リリースの6か月後に削除します。未成年の方は保護者の同意を得てから登録してください。<a href="/privacy.html" target="_blank" rel="noopener">プライバシーポリシー</a>'),
  ('>혜택 받고 출시 알림 신청</button>', '>特典つきでリリース通知に登録</button>'),
  ('alt="두 손을 모으고 부탁하는 하린"', 'alt="両手を合わせてお願いするハリン"'),
  ('<h2>신청 완료! 그리고…<br>설문조사 한 번만 해 주시면 안 될까요?!! 🥺</h2>', '<h2>登録完了！それと…<br>アンケート、1回だけお願いできませんか？！🥺</h2>'),
  ('<p class="sub">5분이면 끝나요. 하린을 더 잘 만드는 데 꼭 쓸게요</p>', '<p class="sub">約6分で終わります。ハリンをもっと良くするために使います</p>'),
  ('>좋아요, 설문 하러 가기</a>', '>いいよ、アンケートに答える</a>'),
  ('>다음에 할게요</button>', '>また今度</button>'),
  ("pill.textContent = (os === 'android' ? 'Android' : 'iOS') + ' · 12월 출시 예정';", "pill.textContent = (os === 'android' ? 'Android' : 'iOS') + ' · 近日公開';"),
  ("'이메일 또는 휴대폰 번호(010-0000-0000)를 적어 주세요'", "'メールアドレスを正しく入力してください'"),
  ("'개인정보 수집·이용에 동의해 주세요'", "'プライバシーへの同意にチェックしてください'"),
  ("'잠시 후 다시 시도해 주세요 ('", "'しばらくしてからもう一度お試しください ('"),
  ("'네트워크 오류예요. 잠시 후 다시 시도해 주세요'", "'ネットワークエラーです。しばらくしてからもう一度お試しください'"),
 ],
}

COMMON = [
  # 채널: 해외판은 인스타 유입만 A-1 'Instagram'으로 미리 채운다
  ("const CH = { x: 'X(트위터)', dc: '디시인사이드', et: '에브리타임', meta: '스레드·인스타그램', ig: '스레드·인스타그램' };", "const CH = { meta: 'Instagram', ig: 'Instagram' };"),
  # 연락처는 이메일만
  ("const normalize = (raw) => { const t = raw.trim(); if (EMAIL.test(t)) return t.toLowerCase(); const d = t.replace(/\\D/g, ''); return PHONE.test(d) ? d.replace(/^(\\d{3})(\\d{3,4})(\\d{4})$/, '$1-$2-$3') : null; };", "const normalize = (raw) => { const t = raw.trim(); return EMAIL.test(t) ? t.toLowerCase() : null; };"),
]

for lang, pairs in T.items():
    out = src
    form = FORMS[lang]
    pairs = pairs + COMMON + [
        ("const FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSfOHMf0OIpitnzPhLal0OWthZ7Zy3aNLv9MTkIc2merU7T8AQ/viewform';", "const FORM = '%s';" % form),
        ("page: 'harin'", "page: 'harin-%s'" % lang),
        ("const KEY = 'feeler_harin_v1';", "const KEY = 'feeler_harin_%s_v1';" % lang),
        ("const source = 'feeler.kr/harin'", "const source = 'feeler.kr/harin/%s'" % lang),
        ("kind: contact.includes('@') ? 'email' : 'phone'", "kind: 'email'"),
    ]
    for a, b in pairs:
        if a not in out:
            raise SystemExit('[%s] 원문에서 못 찾음: %s' % (lang, a[:70]))
        out = out.replace(a, b)
    left = sorted(set(re.findall(r'[가-힣][^<>"\']{0,20}', re.sub(r'<!--.*?-->|//[^\n]*', '', out, flags=re.S))))
    os.makedirs(os.path.join(HERE, lang), exist_ok=True)
    open(os.path.join(HERE, lang, 'index.html'), 'w', encoding='utf-8').write(out)
    print(lang, 'ok, 남은 한글:', left[:10])
