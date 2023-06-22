# 멍결고리
## 간단소개
### 프로젝트 설명
- 반려동물을 키우는 가구가 증가함에 따라 유기되는 동물들도 증가하고있다. 유기동물의 45%는 보호소에서 안타까운 죽음을 맞이하고 있다. 이러한 문제를 해결하고자 프로젝트를 기획하게되었다. 프로젝트 이름은 멍결고리로 보호소, 유기견, 입양자를 연결해준다고 해서 짓게된 이름이다. 멍결고리 서비스는 MBTI를 이용한 유기견 추천, 다양한 페르소나를 가진 유기동물과의 채팅, 컨셉에 맞는 유기견 이미지 생성을 제공하고 있다.
- 
### 프로젝트 기간
- 60일
  
### 팀구성
- 윤예찬
- 이지원
- 박수빈
- 지승엽
- 박상욱
- 고종현

### 내가 맡은 역할 ( 팀장 )
- 기획
- GPT 프롬프트( 페르소나, 대화형식 )
- GPT API를 이용한 Agent 이미지 구현
- Pinecone을 활용한 GPT 장기기억 구축
- 도커파일 작성
- Python 백엔드 구축
- MySQL DB설계, 전체 코드 다듬기
- 사용한 언어 : Python, JQuery, SQL

### 프로젝트 진행 중 마주한 어려움
- GPT 출력 형식을 제어하는것이 가장 어려웠다. 예를들어 행복한 강아지라는 페르소나를 부여한다고 해보자. 내가 질문을하면 행복한 강아지를 연기하며 답변을 해줄것이다. 하지만 욕설 혹은 특정 질문을 하게 되면 "자신은 GPT 인공지능이므로 답변을 해줄 수 없다"라는 말을 한다. 이러한 문제를 해결하기 위해 많은 공부와 시간을 쏟았다. COT(Chain-of-Thought·생각의 연결고리) 기법을 활용하여, 순차적으로 생각하고 결과를 도출해내도록 만들었고, COT 기법 사용시 문제점인 모든 결과를 하나하나 보여주는 것을 해결하기 위해 답변형식을 지정해주었다. 마지막으로 백틱을 통해 영역을 명확히 구분해주었다.
- 방향성이 달라진다는 점이다. 프로젝트 초기에 방향성을 설정하고 진행하였다. 하지만 시간이 지날수록 각자 기억에 왜곡이 일어나고 점점 서로 다른 방향성을 갖게되어 의견이 대립되었다. 이번 경험으로 회의의 중요성과 회의 초반에 방향성을 계속 상기시켜줘야 한다는 것을 깨달았다.

### 개인적으로 성장한 점
- 팀장으로서의 역할의 중요성을 몸소 깨달았다.방향성을 제시하고 업무를 조정하며, 팀원들의 사기를 높혀줘야하는 것 등 다양한 책임이 있음을 알게되었다. 이러한 문제들을 해결하기 위해, 팀원들보다 일찍 출근하여 회의를 준비하고 업무를 체크하여 효율적인 분배를 이끌었다. 또한, 긍정적이고 높은 에너지를 유지하여 팀원들의 사기를 높이는 역할을 수행하였다. 이를 통해 팀 리더십과 조직 관리의 중요성을 깨달았고, 팀원들과의 협업과 조화를 이루는 방법에 대해 배우게 되었다.

### 홍보영상 : [[멍결고리 홍보영상 YouTube 이동하기]](https://www.youtube.com/watch?v=CcHQCNGeMlg)
- 꼭 봐주세요
### 시연영상 : [[멍결고리 시연영상 YouTube 이동하기]](https://www.youtube.com/watch?v=CGVKXz7o-v8)
- 꼭 봐주세요

### 기술스택
![기술스택](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/2d1ef016-cf6d-48b5-b0c1-7173f67f3c46)

### ERD
![7조_ERD](https://github.com/yunyechan9893/SKRookiesProject5-MG/assets/125535111/5d835ec4-539c-4ca0-8e5b-700f7dbb574c)

### 인프라 구성도
![7조_인프라구성도](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/c5c18ae0-ee20-44a3-97f7-ca7923d27d67)

### 서류
- WBS
- 개발기능 정의서
- 요구사항 정의서
- 클라우드 사용계획서
- 프로젝트 계획서
- 회의록
- 기획발표
- 중간발표
- 최종발표

# PPT
![7조_최종발표1](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/8c5dc5a0-6bc5-4f64-85cd-a21783fdbf65)
![7조_최종발표2](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/5f069258-0217-4c46-9a27-f26bf9ad5a5e)
![7조_최종발표3](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/0a7ad401-6bfe-4719-8d1a-b1236e3225a7)
![7조_최종발표4](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/d2895ae5-f2e6-47bf-bc17-2c1fd1a3a850)
![7조_최종발표5](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/5f9fd8f9-5760-48fc-a3ef-e0f6361836a5)
![7조_최종발표6](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/86741561-4af3-415b-b8bc-c2db5a03909d)
![7조_최종발표7](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/d62f9cdf-fe9f-4e65-92d8-6216db2e145d)
![7조_최종발표8](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/be6410db-b8ab-487c-8685-c4d8a736c2a2)
![7조_최종발표9](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/1d9ec2e5-00da-4a14-a0e5-1e2344019700)
![7조_최종발표10](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/cb96134c-bb74-4909-8fb0-97e34d0fb52d)
![7조_최종발표11](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/456786d0-e838-4f95-9793-a25e8db57d41)
![7조_최종발표12](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/ec554458-6e40-412b-8ca8-192f019362fb)
![7조_최종발표13](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/7a492e71-1515-40a4-8463-9dd3e7c5d52f)
![7조_최종발표14](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/abb1d2df-158f-421e-863c-7eafdd2d12d2)
![7조_최종발표15](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/a4458195-7442-4ed2-ba6b-649f91570f9a)
![7조_최종발표16](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/f63e6f9e-d6d2-4270-b3d8-2acf9600a48b)
![7조_최종발표17](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/87d3e4df-2fee-4d06-9b0e-c59ae3881e72)
![7조_최종발표18](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/757fa3a4-3514-4738-a5e1-5bb719adfba4)
![7조_최종발표19](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/8354ce15-e0e6-4c1e-a943-3677f95a5213)
![7조_최종발표20](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/e94a4926-8417-4434-b895-1df75440c690)
![7조_최종발표21](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/50578d40-5bc3-4555-8dba-c4e2fcd6adbd)
![7조_최종발표22](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/9be92f1f-53ff-4d00-ac2d-b1879d0901ac)
![7조_최종발표23](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/5ff07b39-8a27-49be-ac8b-9820953bf0bb)
![7조_최종발표24](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/dc36421c-75d7-45dc-9517-db89701223e3)
![7조_최종발표25](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/0217dfa6-dd05-42dc-b89f-e91c86ef9744)
![7조_최종발표26](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/224f4fd8-ba02-45bf-a453-16f7c37bd8e5)
![7조_최종발표27](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/240d90d6-233e-4fc7-ac04-2b94dd282561)
![7조_최종발표28](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/b6d259d4-a9a2-4356-bea3-579b44e68b86)
![7조_최종발표29](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/036f7354-8247-49f4-83e6-55848a2666b6)
![7조_최종발표30](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/9dbcfbcb-8b4e-4349-8c40-27d4491ce528)
![7조_최종발표31](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/5135caf2-a090-425e-b119-82ed36e54f72)
![7조_최종발표32](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/1b4aea45-4d05-41c3-82eb-817805de1477)
![7조_최종발표33](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/c2c3fbfd-7e36-4f8d-a636-6cd224fd4a82)
![7조_최종발표34](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/afb6d740-d329-491f-8f4d-763dc4df62f5)
![7조_최종발표35](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/329fe434-e665-4fbd-94d5-fc852df96e29)
![7조_최종발표36](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/ddd79e96-2f34-40ba-8fdc-ebacc377a40f)
![7조_최종발표37](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/b2495cb5-0d79-4858-9f39-6ac3b7f42b0f)
![7조_최종발표38](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/32996d4b-691c-4b4f-9524-5cc70eb6ae60)
![7조_최종발표39](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/17603568-5b9f-44ec-b179-071596112b9c)
![7조_최종발표40](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/43aeb70e-17de-48e7-bf74-03022c44fe9b)
![7조_최종발표41](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/5864b185-f495-4526-8b1e-3eb26aedc016)
![7조_최종발표42](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/254cec5f-ab1a-4f8b-89e3-6f9b8bff2abc)
![7조_최종발표43](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/52a7d70e-aef3-40c4-be86-070126566049)
![7조_최종발표44](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/114d220b-8539-48ce-a830-3ec27d58e92f)
![7조_최종발표45](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/b00108fd-1d4d-45c0-95e7-f68e1218d0b0)
![7조_최종발표46](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/d579937b-33dd-4bdd-801c-5862d034f1d8)
![7조_최종발표47](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/658650a0-ca98-4659-899a-4d1c1a805ba3)
![7조_최종발표48](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/2e5eb557-329e-484b-9db9-eaf8cd19a1bb)
![7조_최종발표49](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/a9ea09ea-ef7e-44cc-8d90-9e4b9889ae3f)
![7조_최종발표50](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/72020b55-b6f9-4a2a-bf2f-f60840618999)
![7조_최종발표51](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/69829a42-f1f3-48a9-ba38-4d2314a65763)
![7조_최종발표52](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/6b5465e6-99fd-4eff-a812-02889a697792)
![7조_최종발표53](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/2e6b24bd-1fa0-4a62-9112-5b696c69c53a)
![7조_최종발표54](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/62d79382-aa4b-49e6-ab30-54e559d5d111)
![7조_최종발표55](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/809e26a7-42dd-485a-8c3b-545c623b3ba7)
![7조_최종발표56](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/3c21ff58-9608-4acd-bf7d-fc7dee882372)
![7조_최종발표57](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/1a618803-e92b-4f1a-ba2b-646332fb93e9)
![7조_최종발표58](https://github.com/yunyechan9893/sk_rookies_project5/assets/125535111/6f8ce594-3c93-41c8-adca-cae84f06b6f1)
