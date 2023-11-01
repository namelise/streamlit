import streamlit as st

st.set_page_config(
    page_title='공동교육과정',
    page_icon='👀'
)
menu = st.sidebar.selectbox('MENU', ['로그인', '자기소개', '선택과목 조사', '기타'])
if menu == '자기소개':
    st.title('자기소개')
    st.video('https://www.youtube.com/watch?v=PRFHnSTLwAY')
elif menu == '선택과목 조사':

    st.title('선택과목조사')
    st.subheader('과학')
    st.caption('2개 택')
    지구과학 = st.checkbox('지구과학')
    화학 = st.checkbox('화학')
    물리 = st.checkbox('물리')
    생명 = st.checkbox('생명')
    a=''
    b=0
    if 지구과학:
        a=a+'지구과학 '
        b=b+1
    if 화학:
        a=a+'화학 '
        b=b+1
    if 물리:
        a=a+'물리 '
        b=b+1
    if 생명:
        a=a+'생명 '
        b=b+1

    if b>2:
        st.write('선택과목 초과')
        a=''
    else:
        st.write(a)
    st.subheader('외국어')
    외국어 = st.multiselect('2개 택',['중국어 ', '일본어 ', '독일어 ', '영어 '])
    if len(외국어)>2:
        st.write('2개만 택하시오')
        외국어 = ''
    text = ''
    for value in 외국어:
        text += value+""
    else:
        st.write(text)

    st.write('최종선택 : '+text + a)
    st.image('6554310901b_l.jpg')
elif menu == '기타':
    st.title('기타')
elif menu == '로그인':
    st.title('로그인')
    id = st.text_input('아이디', placeholder='아이디를 입력하시오❤')
    pw = st.text_input('비밀번호', type='password', placeholder='비밀번호를 입력하시오')
    login = st.button('로그인')
    if login:
        if id == 'test123' and pw =='qwer1234':
            st.write('로그인 성공')
            st.balloons()
        else:
            st.write(':red[로그인 실패!]')











# 짜장면 = st.checkbox('짜장면')
# 탕수육 = st.checkbox('탕수육')
# 짬뽕 =  st.checkbox('짬뽕')

# a = ''
# b = ''
# c = ''
# d=''
# if 짜장면:
#     a = a+ '짜장면' 
# if 탕수육:
#     b = b+ '탕수육'  
# if 짬뽕:
#     c = c+ '짬뽕' 
# st.write(a  +b +c)

# 성별 = st.radio('당신의 성별은?',[ '남자', '여자'])
# st.write('당신의 성별은'+성별+'임니다')

# email = st.selectbox(
#     'email을 선택하세요',
#     ['gmail.com', 'naver.com', 'hanmail.com']
# )

# food = st.multiselect('당신이 좋아하는 음식은?', ['피자', '햄버거', '파스타'])
# st.write(food)




# st.write('박준현')








# st.subheader('this is subheader')
# st.header('this is header')
# st.title('this is title')
# st.caption('this is caption')
# st.code('x = 10+20')

# btn = st.button('클릭')
# if btn:
#     st.write('버튼클릭')
# text = '이 버튼을 클릭하면 파일을 다운받을 수 있습니다.'
# download_btn = st.download_button('다운로드', text)
# link_btn = st.link_button('네이버', "https://www.naver.com")
# link_btn = st.link_button('구글', "https://www.google.com")

# checkbox = st.checkbox('동의')
# if checkbox:
#     st.write('동의하셨습니다.')