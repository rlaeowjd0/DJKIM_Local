# 캐릭터 이름 다시 설정
# 주인공(플레이어) : 유저 닉네임 설정 
#여학생 A : 이예진  남학생A : 홍찬동    남학생B : 임준혁
#전학생 : 남진구    귀신 1 : 최지호


define ch_주인공 = Character("설정", color ="#FFFFFF" )
define ch_여학생A = Character("예진", color ="#FFFFFF")
define ch_시스템 = Character("", color = "#FFFFFF")
define ch_남학생A = Character("홍찬동", color = "#FFFFFF")
define ch_남학생B = Character("임준혁", color = "#FFFFFF")
define ch_귀신1 = Character("지호", color = "#FFFFFF")
define ch_할머니 = Character("수상한 할머니", color = "#FFFFFF")
define ch_정체모름 = Character("???", color = "#FFFFFF")
define ch_소년 = Character("소년", color = "#FFFFFF")
define ch_담임 = Character("담임선생님", color = "#FFFFFF")
define ch_전학생 = Character("남진구", color = "FFFFFF")

image bg 주인공집심야 = "BG/주인공집심야.jpg"
image bg 주인공집 = "BG/주인공집.jpg"
image bg 교실 = "BG/교실.jpg"
image bg 등교길 = "BG/등교길.jpg"
image bg 등교길1 = "BG/등교길1.jpg"
image bg 노을 = "BG/노을노을.jpg"
image bg 얼굴 = "BG/얼굴.jpg"
image bg 해저무는교실 = "BG/해저무는교실.png"

image scg_주인공: 
    im.FactorScale("Charactor/주인공/주인공.png", 0.35)
    yalign 0.0


image scg_주인공걱정하는표정:
    im.FactorScale("Charactor/주인공/주인공걱정하는표정.png", 0.35)
    yalign 0.0


image scg_주인공당황하는표정:
    im.FactorScale("Charactor/주인공/주인공당황하는표정.png", 0.35)
    yalign 0.0

image scg_주인공멍한표정:
    im.FactorScale("Charactor/주인공/주인공멍한표정.png", 0.35)
    yalign 0.0

image scg_주인공놀란표정:
    im.FactorScale("Charactor/주인공/주인공놀란표정.png", 0.35)
    yalign 0.0


image scg_여학생A: 
    im.FactorScale("Charactor/여학생A/여학생A.png", 0.35)
    yalign 0.0

image scg_여학생A공포에질린:
    im.FactorScale("Charactor/여학생A/여학생A공포에질린.png", 0.35)
    yalign 0.0

image scg_여학생A웃는모습:
    im.FactorScale("Charactor/여학생A/여학생A웃는모습.png", 0.35)
    yalign 0.0

image scg_여학생A화난표정:
    im.FactorScale("Charactor/여학생A/여학생A화난표정.png", 0.35)
    yalign 0.0


image scg_홍찬동:
    im.FactorScale("Charactor/홍찬동.png", 0.35)
    yalign 0.0

image scg_준혁:
    im.FactorScale("Charactor/준혁.png", 0.35)
    yalign 0.0

image scg_남진구:
    im.FactorScale("Charactor/남진구.png", 0.35)
    yalign 0.0



define left =Position(xalign = 0.0)
define right =Position(xalign = 1.5)
define center =Position(xalign = 0.5)

    #define bunker = 0

label start:
    $ renpy.movie_cutscene("media/인트로.mpg")

   


    

    
        
label start1:

    scene bg 주인공집심야 with fade

    ch_정체모름 "크..."
    
    ch_정체모름 "내가 이 봉인에서 풀려난다면..."

    ch_정체모름 "전...부... 죽여버리겠다..."


    

label start2:

    scene bg 주인공집 with fade

    ch_시스템 "악몽을 꾼것인지 식은땀을 흘리며 일어나는 소년"
    
    ch_시스템 "주위를 둘러 보며 방금의 상황이 꿈인 것을 깨닫고 안도한다."

    #(캐 : 주위를 둘러보고 꿈인 것을 깨닫는지 안도하는 표정)
    show scg_주인공 at left with dissolve

    ch_소년 "하... 꿈이였나..."

    hide scg_주인공 with dissolve



label start3:
    scene bg 등교길 with fade

    #(배경 : 이른 아침. 등교 하는 학생들)

    ch_시스템 "이른 아침. 간밤에 꾼 악몽 때문에 생각에 빠져 정신없이 걷고 있었다."

    scene bg 등교길1 with fade
    
    ch_시스템 "그 뒤로 누군가 달려오는 인기척이 느껴졌는데."


    #(캐 : 숨이 찬지 잔뜩 찡그린 표정 (그래픽 완료시 표정 다시 추가))
    show scg_여학생A at right with dissolve
    ch_여학생A "야! 넌 치사하게 혼자 가냐! 숨 차 죽겠네."
    hide scg_여학생A with dissolve


    #(생각에 빠진 듯 멍한 모습)
    show scg_주인공멍한표정 at left with dissolve
    ch_주인공 "......"
    hide scg_주인공멍한표정 with dissolve

    show scg_여학생A화난표정 at right with dissolve
    ch_여학생A "야 내 말 듣고 있어?"
    hide scg_여학생A화난표정 with dissolve

    show scg_주인공놀란표정 at left with dissolve
    ch_주인공 "깜짝이야. 언제 왔어? 소리 좀 지르지마. 그리고 내이름은 '야'가 아니잖아.
    내 이름은..."
    hide scg_주인공놀란표정 with dissolve

    ch_시스템 "플레이어의 이름을 말해주세요."

    #플레이어 닉네임 설정 구현 


    show scg_주인공 at left with dissolve
    ch_주인공 "내 이름은 ' ' 이잖아. 똑바로 불러."
    hide scg_주인공 with dissolve

    show scg_여학생A at right with dissolve
    ch_여학생A "예민하기는! 그래, (유저설정네임). 아침부터 대체 무슨 생각을 하길래 사람이 오는
    것도 모르는 거야?"
    hide scg_여학생A with dissolve

    show scg_주인공 at left with dissolve
    ch_주인공 "아 지난밤에 꿈을 꿨는데 영 찝찝해서. 별거 아니야."
    hide scg_주인공 with dissolve
    
    show scg_여학생A at center with dissolve
    ch_시스템 "이 친구의 이름은 이예진. 어릴 적부터 같은 마을에서 함께 자란 소꿉친구로 현재
    같은 고등학교에 진학해 올해는 운 좋게 같은 반이 되었다."
    hide scg_여학생A with dissolve

    show scg_여학생A at right with dissolve
    ch_여학생A "별일이네. 네가 꿈을 다 꾸고. 아무튼 일단 교실 가서 이야기하자. 잘못하면 지각하겠어."
    hide scg_여학생A with dissolve

    scene bg 교실 with fade

    ch_담임 "자, 아침 조례는 이걸로 끝. 너무 떠들지 말고 조용히 다음 수업 준비하고 있어라."

    ch_시스템 "선생님이 출석부를 챙겨 나가자마자 시끄러워지는 교실. (유저네임)의 자리로
    다가오는 남학생 두명"

    show scg_홍찬동 at center with dissolve
    ch_남학생A "(유저네임). 주말 잘 보냈냐?"
    hide scg_홍찬동 with dissolve

    show scg_준혁 at center with dissolve
    ch_남학생B "다들 좋은 아침이야!"
    hide scg_준혁 with dissolve

    show scg_홍찬동 at left with dissolve
    show scg_준혁 at right with dissolve
    ch_시스템 "홍찬동과 임준혁은 중학교에서 만난 친구들로 우연찮게 같은 고등학교에 진학했다."

    ch_시스템 "찬동은 수다스럽고 소문이나 재미난 이야기들에 관심이 많으며, 준혁은 성격
    이 호탕하고 아버지의 영향을 받아 어릴 적부터 운동을 배운 친구인지라 또래보다 키도 크고
    덩치도 우람한 편이다."

    hide scg_홍찬동 with dissolve
    hide scg_준혁 with dissolve

    ch_시스템 "예진이를 포함해 우리 넷은 괴담, 미스터리 등에 관심이 많아 학교에서 동아리
    활동 시간에 미스터리 동아리를 만들어 함께 활동하면서 생각보다 더 사이좋게 지내고 있다."

    show scg_주인공 at left with dissolve
    ch_주인공 "어, 좋은아침이야!. 주말 동안 재밌는 일이 없어서 심심해 죽는 줄 알았어."
    hide scg_주인공 with dissolve

    show scg_홍찬동 at right with dissolve
    ch_남학생A "그럴 줄 알았어! 안 그래도 이 형님이 재미난 이야기를 하나 주워듣고 왔단 말이야."
    hide scg_홍찬동 with dissolve

    show scg_주인공 at left with dissolve
    ch_주인공 "그게 뭔데?"
    hide scg_주인공 with dissolve


    show scg_홍찬동 at right with dissolve 
    ch_남학생A "어제 옆 동네에 볼일이 있어서 잠시 다녀왔었는데 어떤 애들이 이야기하는 걸 들
    었거든? 주변골목길에 오래된 물건들을 파는 할머니가 있다고 해서 가봤더니 정말 있더라고.
    한번 가서 뭘 파는지 구경이라도 해보는 건 어떠냐?"
    hide scg_홍찬동 with dissolve

    show scg_주인공 at left with dissolve
    ch_주인공 "그래? 혹시 막 귀신 씌인 물건 파는 거 아냐?"
    hide scg_주인공 with dissolve

    show scg_여학생A웃는모습 at right with dissolve
    ch_여학생A "너희 나 빼고 무슨 이야기를 그렇게 재밌게 해?"
    hide scg_여학생A웃는모습 with dissolve

    show scg_홍찬동 at center with dissolve
    #(음흉한 표정)
    ch_남학생A "왔어? 재밌는 이야기를 좀 하고 있었지~ 흐흐흐흐"
    hide scg_홍찬동 with dissolve


    show scg_여학생A at right with dissolve
    ch_여학생A "그게 뭔데? 또 이상한 거 아냐?"
    hide scg_여학생A with dissolve

    show scg_홍찬동 at center with dissolve
    ch_남학생A "비밀이지~ 나중에 가보면 알아!"
    hide scg_홍찬동 with dissolve

    show scg_주인공 at left with dissolve
    ch_주인공 "좋아, 학교 마치고 다 같이 가보자."
    hide scg_주인공 with dissolve

    scene bg 노을 with fade
    ch_시스템 "찬동이를 앞장세워 '소문의 할머니' 가 있다는 골목을 찾아갔다."

    #(배경 : 골목 중간쯤 바닥 위에 천을 깔고 물건을 늘어놓은 채 앉아있는 할머니가 보인다.)
    ch_시스템 "한적한 주택가의 골목들 중 유독 어두컴컴해 보이는 골목으로 들어서는 주인공 일
    행."

    ch_시스템 "골목 중간쯤 바닥 위에 천을 깔고 물건을 늘어놓은 채 앉아있는 할머니가 보인다."

    show scg_홍찬동 at right with dissolve
    ch_남학생A "저기 저 할머니야."
    hide scg_홍찬동 with dissolve

    show scg_준혁 at center with dissolve
    ch_남학생B "왜 저런 곳에서 물건을 파는 거지? 개미 새끼 한 마리도 얼씬거리지 않을거 같은데."
    hide scg_준혁 with dissolve

    show scg_홍찬동 at right with dissolve
    ch_남학생A "그러니까 재밌는 거지. 한번 가보자."
    hide scg_홍찬동 with dissolve

    menu :
        
        "안돼. 위험 할 수도 있어! 돌아가자.":
            $ bunker = 1
            jump 선택1

           
           
        "호기심을 이기지 못하고 할머니에게 다가간다.":
            $ bunker = 0
            jump 선택2
              

label 선택1:
    # <Bad Ending 1. 겁 많은 소년>
    if bunker == 1:
        
        ch_시스템 "위험 할 수도 있다는 생각에 아이들을 만류하고 돌아가자고 하였다."


        show scg_홍찬동 at right with dissolve
        ch_남학생A "에? 여기 까지 왔는데 그냥 돌아가자고?"
        hide scg_홍찬동 with dissolve

        show scg_주인공 at left with dissolve
        ch_주인공 "그래 위험 할 수도 있는데 그냥 돌아가자."
        hide scg_주인공 with dissolve

        show scg_홍찬동 at right with dissolve
        ch_남학생A "하... 쫄보 새끼 그래 그냥 돌아가자."
        hide scg_홍찬동 with dissolve

        scene bg 얼굴 with fade




        return

label 선택2:
    if bunker == 0:

        ch_시스템 "일행을 이끄는 찬동. 골목 안, 할머니에게로 다가가는 아이들."

        #(배경 : 아이들을 둘러보며 킬킬 음침하게 웃는 할머니의 모습.)
        ch_시스템 "할머니는 다가오는 우리를 보며 음침하게 웃고있었다."

        #음침한 표정
        ch_할머니 "클클... 무슨 일로 왔누?"

        show scg_주인공 at left with dissolve
        ch_주인공 "오래된 물건을 판다고 하셔서요. 살만한 게 있을까 해서..."
        hide scg_주인공 with dissolve


        ch_할머니 "그래... 보다시피 이런 오래된 골동품들 뿐이란다. 마음에 드는 것이 있느냐?"

        #(배 : 천 위에 놓여있는 오래된 물건들. 볼펜 같은 필기구나 손거울, 머리핀, 책등이 놓여있다.)

        ch_시스템 "천 위에는 볼펜 같은 필기구나 손거울, 머리핀, 책등이 놓여있다. 모두 너무 오래되어 팔릴 것 같지 않은 물건들이다."

        ch_시스템 "한참을 고민하던 (유저네임)이 손가락으로 물건을 가리키면 말했다."

        show scg_주인공 at left with dissolve
        ch_주인공 "이게 재밌어 보이는데... 얼마에요?"
        hide scg_주인공 with dissolve

        menu :
        
            "낡은 고서":
                $ bunker = 1
                jump 낡은고서

           
           
            "조금 금이 가있는 손거울":
                $ bunker = 0
                jump 손거울

label 낡은고서:
    if bunker == 1:
        #여전히 킬킬 웃는 모습
        ch_할머니 "그래, 그것이 마음에 들었구나... 그렇단 말이지... 옛다,
        그냥 가저가거라."

        ch_시스템 "할머니는 낡은 고서를 집어들고는 우리에게 건내주었다."

        ch_시스템 "아이들은 서로 눈치만 보다가 감사하다는 말과 함께 낡은 고서를 챙겨 후다닥 골목
        을 빠져나갔다."

        ch_시스템 "뒤에서 할머니가 그 모습을 바라보며 여전히 음침하게 웃고 있다."
      
        #(배경 : 해가 져가는 늦은 오후 시간 방과 후 교실 배경)
        scene bg 해저무는교실 with fade

        ch_시스템 "책상을 붙여 옹기종기 둘러 앉아 있는 아이들 그중 (유저네임)앞에 놓여있는
        오래되고 낡은 책이 눈에 띈다."
      
        #(캐 : 고서)

        ch_시스템 "낡은 책 표지 위에는 '   ' 라고 적혀져 있다."

        #약간 들뜬 모습
        show scg_여학생A at right with dissolve
        ch_여학생A "빨리 읽어보자! 단순한 무서운 이야기 아냐?"
        hide scg_여학생A with dissolve

        ch_시스템 "예진의 재촉에 고개를 끄덕이며 책 첫장을 펼치는 (유저네임)"

        ch_시스템 "모두 몸을 기울이며 책 안을 보기 위해 집중하는 순간 눈 앞에 번쩍이는 빛."

        ch_시스템 "밝은 빛 때문에 눈을 감았다 뜨자 여전히 같은 교실 안이다."

        ch_주인공 "뭐야! 방금 엄청 밝은 빛이 났던거 같은데"

        #(혼란스러워 하는 표정)
        show scg_여학생A공포에질린 at right with dissolve
        ch_여학생A "아까 그 불빛은 뭐지? 전등 불빛이 아닌 것 같던데..."
        hide scg_여학생A공포에질린 with dissolve

        #(약간 실망한 모습)
        show scg_홍찬동 at center with dissolve
        ch_남학생A "뭐야... 그 소문이 사실이 아니었나 보네."
        hide scg_홍찬동 with dissolve


        show scg_여학생A at right with dissolve
        ch_여학생A "무슨 말이야?"
        hide scg_여학생A with dissolve

        show scg_홍찬동 at center with dissolve
        ch_남학생A "아까 그 물건 파는 할머니 말이야. 사실은 인간이 아니라는 소문이 돌았거든. 그
        할머니가 파는 물건들을 산 사람들은 모두 행방불명되거나 정신이 이상해진대. 행방불명된 사
        람들은 사실 다른 세계로 그 할머니가 보내버린 거고"
        hide scg_홍찬동 with dissolve

        #(이상한 웃음소리를 내며 음침한 표정을 지음)
        show scg_홍찬동 at center with dissolve
        ch_남학생A "넘어간 사람들은 거기 사는 괴물이 잡아 먹는다는 거야. 아까 불빛이
        번쩍하길래 우리도 다른 세계로 넘어가는 줄 알았지... 크크크..."
        hide scg_홍찬동 with dissolve

        show scg_준혁 at center with dissolve
        ch_남학생B "너 말 다했냐? 이 새끼가 진짜!"
        hide scg_준혁 with dissolve

        ch_시스템 "순식간에 달려들어 찬동의 멱살을 잡은 준혁과 놀라서 그들을 말리려 하는 예진"

        ch_시스템 "원래부터 욱하는 기질이 있는 준혁과 성격이 가볍고 잘 깐족거리는 타입의 찬동은 평소에도
        별것 아닌 일로 자주 투닥거렸지만 오늘은 유독 서로가 예민해 보인다."

        ch_시스템 "말리기도 피곤해 잠시 시선을 돌린 창 밖 운동장에 누군가가 서있는 모습이 보였다."

        show scg_주인공 at left with dissolve
        ch_주인공 "저 사람은..."
        hide scg_주인공 with dissolve

        ch_시스템 "창 밖 텅 빈 운동장 위에 서있는 왜소하고 마른 남학생의 모습. 어딘가 음침하고
        우울해 보인다."

        show scg_주인공 at left with dissolve
        ch_주인공 "전학생...?"
        hide scg_주인공 with dissolve

        show scg_여학생A공포에질린 at right with dissolve
        ch_여학생A "너도 가만있지 말고 좀 말려줘! 얘네 이러다가 정말 크게 싸움 나게 생겼다니까?"
        hide scg_여학생A공포에질린 with dissolve

        show scg_여학생A at right with dissolve
        ch_여학생A "너 내 말 듣고 있는 거야? 도대체 뭘 보고 있... 어, 전학이잖아?"
        hide scg_여학생A with dissolve

        show scg_주인공 at left with dissolve
        ch_주인공 "저 애 어느 순간부터 계속 결석 아니었나?"
        hide scg_주인공 with dissolve

        show scg_여학생A at right with dissolve
        ch_여학생A "그러게... 근데 저 애 말이야, 좀 이상해. 처음 봤을 때부터 등에 작은걸 
        달고 다녔단 말이지"
        hide scg_여학생A with dissolve

        ch_시스템 "할머니가 제법 영험한 무당이었던 예진은 우리가 볼 수 없는 것들을 종종 보곤
        한다."

        ch_시스템 "예진은 지난 1학기, 전학생이 처음 우리 학교로 첫 등교한 순간부터 그 아이에
        게 이상한 것이 붙어있다고 말해왔지만 딱히 친분이 없는 우리로서는 대뜸 전학생에게 이상한
        것이 붙어있다고 참견하기도 애매해 망설이고만 있던 찰나"

        ch_시스템 "어느 순간부터 전학생이 계속해서 결석을 했고 그 후로 전학생을 볼 수 없어 잠시
        잊고 있었다. 얼굴을 보는 것은 거의 다섯 달 만에 보는 것 같다."

        show scg_여학생A공포에질린 at right with dissolve
        ch_여학생A "학교를 왜 안 나왔을까? 어라! 저게 저렇게 컸던가? 위험해!"
        hide scg_여학생A공포에질린 with dissolve

        ch_시스템 "그 말을 끝으로 (유저네임)가 미처 말릴 틈도 없이 뛰쳐나가는 유진.말다
        툼을 벌이며 싸우고 있던 찬동과 준혁도 당황하며 쳐다 보았다."

        show scg_준혁 at center with dissolve
        ch_남학생B "쟤 어디 가는 거야?"
        hide scg_준혁 with dissolve

        show scg_주인공당황하는표정 at left with dissolve
        ch_주인공 "운동장에 전학생이 와있어서 뛰쳐나갔어. 등 뒤에 이상한 게 붙어있다고..."
        hide scg_주인공당황하는표정 with dissolve

        #찝찝해 보이는 표정
        show scg_준혁 at center with dissolve
        ch_남학생B "아직도 그런 소리를 한단 말이야?"
        hide scg_준혁 with dissolve

        show scg_주인공 at left with dissolve
        ch_주인공 "예진이가 그런 것에 대해 함부로 말하는 애가 아니잖아. 분명 정말 문제가
        있어서일 거야. 일단 따라 나가 보자."
        hide scg_주인공 with dissolve

        ch_시스템 "뒤늦게 예진을 따라 운동장으로 향한 주인공과 찬동, 준혁. 운동장 한가운데
        에서 예진과 전학생이 마주 보고 이야기를 나누고 있다."

        ch_시스템 "전학생은 어딘지 모르게 불안한 것인지 몸을 떨면서 안절부절하고 있었다."

        ch_시스템 "예진은 교실에서 나갈 때와 다르게 약간 화가 나있었다."

        show scg_여학생A화난표정 at right with dissolve
        ch_여학생A "너, 내 말 알아듣기는 해? 네 등에 있는 그것 해결하지 않으면 그대로 네가 잡아
        먹힐 거라고."
        hide scg_여학생A화난표정 with dissolve

        #무언가에 겁먹은 표정
        show scg_남진구 at left with dissolve
        ch_전학생 "어떻게... 어떻게 온 거야? 우린 다 죽을 거야..."
        hide scg_남진구 with dissolve

        show scg_여학생A화난표정 at right with dissolve
        ch_여학생A "아까부터 대체 무슨 소리야? 여긴 학교고 계속 무단결석한 건 너잖아. 그리고 나
        는 지금 네 등에 붙어있는 것에 대해 말하고 있는 거거든? "
        hide scg_여학생A화난표정 with dissolve

        show scg_남진구 at left with dissolve
        ch_전학생 "그게 아니야... 너희도 결국... 이곳에 갇히고 만 거야..."
        hide scg_남진구 with dissolve

        ch_시스템 "여전히 공포감에 젖어 동문서답하는 전학생을 이상하게 바라보는 등장인물들."

        ch_시스템 "덜덜 몸을 떨던 전학생이 갑자기 주위를 두리번거리다 어느 한 곳을 바라본다."


        ch_시스템 "전학생이 바라보는 곳을 쳐다 보자 분명 교실에 있어야 할 책이 바닥 에 떨어져있었다."

        show scg_주인공놀란표정 at left with dissolve            
        ch_주인공 "응? 왜 이 책이 여기있지? 교실에서 가져나오지 않았는데? 예진이가 들고왔었나?"
        hide scg_주인공놀란표정 with dissolve
        ch_시스템 "주인공이 책을 주워 들다가 책이 펼쳐 졌는데"
        
        ch_시스템 "책에 내용이 사라졌다!"

        ch_시스템 "준혁 이 (유저네임)에게 다가왔다."

        show scg_준혁 at right with dissolve
        ch_남학생B "뭐야? 책 두고온거 아니였어? 가지고 왔었나?"
        hide scg_준혁 with dissolve

        show scg_주인공 at left with dissolve
        ch_주인공 "아니 두고 왔었는데 여기 떨어져 있었어 그것보다 책에 내용이 모두 사라져있어"
        hide scg_주인공 with dissolve

        show scg_준혁 at right with dissolve
        ch_남학생B "무슨 뜬금없는 소리야"
        hide scg_준혁 with dissolve

        ch_시스템 "(유저네임)이 준혁에게 책을 건네주었다."

        show scg_준혁 at right with dissolve
        ch_남학생B "이...이게 뭐야? 책이 왜 백지가 되었냐?"
        hide scg_준혁 with dissolve

        show scg_주인공 at left with dissolve
        ch_주인공 "나도 모르겠어 이게 무슨일이 일어난건지 애초에 난 이책 자체를 교실에 놔두고 왔
        었단 말이야. 분명 책상에다 두고 나왔는데..."
        hide scg_주인공 with dissolve

label 손거울:
    if bunker == 0:
        # Bad Ending 2. 아무 일도 일어나지 않았다.

        ch_할머니 "그래, 그것이 마음에 들었구나... 그렇단 말이지... 옜다,
        그냥 가져가거라."

        ch_시스템 "할머니느 조금 금이 가있는 손거울을 집어들고는 우리에게 건내주었다."

        ch_시스템 "아이들은 서로 눈치만 보다가 감사하다는 말과 함께 조금 금이 가있는 손거울을 챙겨 
        후다닥 골목을 빠져나갔다."

        ch_시스템 "뒤에서 할머니가 그 모습을 바라보며 여전히 음침하게 웃고 있다."

        show scg_여학생A공포에질린 at right with dissolve
        ch_여학생A "뭐야... 저 할머니 뭔가 이상해 소름끼쳐"
        hide scg_여학생A공포에질린 with dissolve

        show scg_준혁 at center with dissolve
        ch_남학생B "그러게 아까부터 이상하게 웃는것도 그렇고 영 맘에 들지 않네."
        hide scg_준혁 with dissolve

        show scg_주인공 at left with dissolve
        ch_주인공 "뭐 아무일도 없었으면 됬지. 그나저나 이 손거울은 뭘까?"
        hide scg_주인공 with dissolve

        show scg_홍찬동 at center with dissolve
        ch_남학생A "어디에 쓰였던 물건일까?"
        hide scg_홍찬동 with dissolve


        ch_시스템 "아이들은 손거울에 변화가 있을까 하고 지켜 보았지만 아무일도 일어나지 않았다."

        show scg_주인공 at left with dissolve
        ch_주인공 "뭐야 설마 그냥 손거울이잖아. 에이 괜히 시간만 버렸네."
        hide scg_주인공 with dissolve






        return




