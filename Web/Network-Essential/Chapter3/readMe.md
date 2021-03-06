## TCP/IP 통신구조

네크워크의 본질적 기능, 미시적 관점에서 필요한 내용

---
### 1. 가변길이 서브넷 마스크

* 서브넷 별로 서브넷 마스크의 길이를 다르게 할 수 있다.
* 가변길이 서브넷 마스크 : VLSM(Variable, Length Subnet Masking)

* subnet mask의 len을 자유롭게 바꿀 수 있다면, 서브넷 별로 접속할 컴퓨터의 수를 유연하게 결정할 수 있다. 

### 2. CIDR

* Classless Inter-Domain Routing
* 가변길이 서브넷 마스크를 기반으로 하는 기술, 근데 약간 다르다.
* 네트워크 마스크가 짧다고 간주함으로써 여러 개의 네트워크에 대한 전송 규칙을 통합하는 기술이다!

![image](./source/vlsm.JPG)


### 3. MAC 주소 

* mac : media access control address
* 물리주소
* 다른 것과 중복되지 않는 유일한 값을 가져야 한다는 것이 원칙
* 16진수 6개의 값으로 표현됨
* 초기 세 개의 값은 제조사를 나타내는 vender id, 그 다음은 기종 id, 마지막 두 개의 값은 시리얼 id
* MAC주소를 고쳐쓰는 제품들이 있다라, 개쳅별로 사용하는 주소가 유일하다는 것이 반드시 보장되지는 않는다

* 이전 이더넷 MAC 주소 사용법
    * 전체에게 동일한 데이터를 보내가 MAC 주소가 자신 앞으로 돼있는 경우에만 수신, 그렇지 않으면 무시하는 구조로 통신이 이뤄진다. 엄청나게 비효율적인 방법

* 현재의 이더넷 MAC 주소 사용법
    * 허브/스위치가 어떤 포트에 어떤 MAC 주소가 연결되어 있는지 기억하고 있으므로, 일종의 port-MAC(key-value) table에서 해당 MAC을 찾아서 해당 기기에만 데이터를 보낸다. 


### 4. ARP가 필요한 이유

* 이더넷 하드웨어 끼리는 MAC 주소 기반 통신
* TCP/IP 통신에서는 IP 주소 사용 
* IP 패킷을 상대에게 보내기 위해 컴퓨터는 상대방의 IP 주소의 네트워크부를 확인한다.

    * 자신의 네트워크와 같은 소속?이면 물리적으로 연결되어 있다고 판단한다. 
        * 그 다음에는 IP 주소에서 MAC 주소를 도출하는 동작을 수행!(여기서도 ARP 사용)

    * 대상이 다른 네트워크에 있는 경우, 그 IP 패킷을 다음 라우터로 넘겨야 한다. 
        * 이때 라우터의 IP 주소에서 MAC 주소를 얻을 필요가 있다. 
        * 이 동작에 ARP(Adrdress Resolution Protocol) 프로토콜이 사용됨
        * 아 이해했다. 라우터는 단지 경유지일 뿐.
        * 그런데 여러 개의 라우터에 연결되어 있을 때, 어느 한 라우터로 연결된 다른 네트워크들 중에 원하는 목적지가 없을 수 있다.
        * DFS나 BFS 방식으로 탐색하는 방식으로 통신-처리가 될라나? 여기서도 아직은 내가 모르는 최적화가 있겠다. 


* ARP에서는 브로드캐스트가 사용된다. 
    * 혹시 너님들, IP가 이건가요?(request)
        * 아니요, 무시한다.
        * 예, 제 IP가 맞습니다. 제 MAC 주소 보내드립니다.(reply)
    * 이러한 방식으로 MAC 주소를 알아낸다.

### 5. 도메인명

* 도메인명의 개요
    * 인터넷 도메인명은 전세계에서 유일하도록 관리되고 있다.
    * ICANN에서 최상위 도메인, TLD, Top Level Domain을 관리하고 있다.
    * .com이나 .net은 VeriSign이라는 미국 기업이 관리. .kr은 한국인터넷진흥원에서 윤영하는 한국 도메인에서 관리.
    * 관리조직(레지스트리)는 해당 TLD를 관리함과 동시에 이를 위한 DNS를 운옇아고 있다. 
    * 도메인명 등록 대행지 : 레지스트리와 계약해서 도메인을 등록하고자 하는 사람으로부터 신청을 받는다. 
    
* 각종 도메인 
    * .info, .biz, .name 등의 새로운 gTLD가 이용되기 시작. 

* 도메인명의 구조
    * www(3단계 도메인).example(2단계 도메인, SLD).com(최상위 도메인, TLD)

* gTLD : 분야별(.com, .net, .org), ccTLD : 국가별(.kr, .uk , .de)
    * .com : 상거래 대상 
    * .net : 인터넷 서비스 대상
    * .org : 그 외 조직 대상

### 6. 라우팅과 기본 게이트웨이

* 라우팅의 동작 개념
    * 라우터로 패킷을 전송하는 것, 라우팅
    * 무엇을 어디로 전송하면 될지 결정하는 전송 규칙에 따라 수행
        * 여기서 중요한 것 라우팅 테이블 (수신처의 네트워크, 그 네트워크에 대한 발송 방법으로 구성)
    * 라우터가 발신처로부터 패킷을 받으면 그 수신처로 표시돼있는 IP 주소에 서브넷마스크를 적용해 네트워크 주소를 추출한다. 그리고 라우팅 테이블에서 그 네트워크에 대한 규칙을 찾는다. 그 규칙에 맞게 전송한다. 

* 기본 게이트웨이
    * 네트워크를 사용하는 대부분의 PC에 설정되어 있다.
    * 자신이 소속된 네트워크 이외에 보내려는 패킷에 대해 어디로 보내면 좋을지 정보를 갖고 있지 않을 때의 전송처.
    * 즉, 보낼 곳을 모르는 때에 우선 전송해두는 곳.

### 7. 정적 라우팅, 동적 라우팅

* 네트워크 구성이 변하면 라우팅 테이블 갱신 필요

* 정적 라우팅, 수동으로 관리, 네트워크 규모가 작을 때, 변화의 빈도가 적을 때 사용

* 동적 라우팅, 라우터끼리 라우터 정보를 서로 교환


### 8. 라우팅 프로토콜

* 라우팅 테이블을 동적으로 갱신하는 동적 라우팅에서 사용하는 프로토콜
    * 라우팅 끼리 경로 정보를 교환한다.
    * 수집한 경로 정보에서 최적 경로를 골라낸다.
    * 크게 IGP(Interior Gateway Protocol) and EGP(External)이 있다.
    * ISP나 한 대기업이 담당하는 대규모 네트워크를 AS(Autonomous System)이라고 하는데
    * IGP는 AS 내의 라우팅에 이용, EGP는 AS 간의 라우팅에 이용

* IGP
    * RIP/RIP2 : 소규모 네트워크에 이용, 단순히 통과하는 라우터의 수가 적은 경우 선택
    * OSPF : open shortest path first : 네트워크 속도 등도 고려해서 최적 경로 선택 

### 9. DHCP 서버

* 자동으로 네트워크를 설정하는 구조
* Dynamic host configuration protocol : 네트워크에 접속되어 있는 컴퓨터에 대한 필요한 네트워크 설정 정보를 자동으로 배포하기 위한 구조.

* 이것을 사용하기 위해서는 컴퓨터에 DHCP 클라이언트 기능이 탑재되고, 네트워크에 DHCP 서버가 있어야 한다. 

* DHCP 로 설정할 수 있는 주요 정보
    * IP, subnet mask, gateway, DNS server's IP

* 소규모 사무실이나 가장에서 사용하는 대부분의 라우터는 DHCP 서버 기능을 갖고 있다. 

* DHCP 동작 흐름

    * DHCP는 아직 컴퓨터에 IP 주소 등의 네트워크 설정이 되어 있지 않은 시점에 사용하므로 IP 주소를 지정해서 하는 일반적인 통신을 이용하지 않음

    * 브로드케스팅을 잘 사용해서 DHCP 서버와 주고 받는다.

    * 1. DHCP 클라이언트 -> DHCP discover message 를 broadcasting -> to that network
        * DHCP 서버에 대해 IP 주소를 호출하는(내 IP 알려줘) 의미가 있다.
    * 2. 위 message를 수신한 DHCP 서버는 설정정보의 후보(IP)를 결정, DHCP offer message를 보낸다 -> to client which sent the broadcast message
    * 3. client가 offer message를 받고 해당 설정정보를 사용하겠다고 DHCP 요청을 broadcasting 한다
    * 4. DHCP 서버가 DHCP Ack를 client에 보낸다.(해당 IP를 사용해도 좋다는 승낙을 했다고)
    * 5. 이제서야 Client가 설정정보를 사용해서 통신을 시작한다. 


### 10. TCP/IP 동작을 확인하는 데 사용하는 편리한 명령어들

* ping : 지정된 컴퓨터까지 IP로 통신 가능 여부를 확인하는 방법
* nslookup, dig 명령어 : DNS에 질의해서 도메인명을 얻고 DNS가 정확하게 동작하는지 여부를 확인하는 명령어 
    * window 콘솔에서 nslookup를 입력하면 일종의 cli가 작동하네

    