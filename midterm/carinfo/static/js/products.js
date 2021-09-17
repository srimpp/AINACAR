$(document).ready(function() {
  	$("#content1").html('<a id="전장" href="#a" title="">전장</a>');
  	$("#content1 #전장").tooltip({ content : "<span id='price'>전장(Overall Length)</span><p style='font-size:15px;'>자동차의 길이를 자동차의 중심면과 접지면에 평행하게 측정했을 경우 범퍼와 후미등을 포함한 최대 길이다. <img width='200' src='/static/images/설명/전장.png'/></p>" });
  	
  	$("#content2").html('<a id="전고" href="#a" title="">전고</a>');
  	$("#content2 #전고").tooltip({ content : "<span id='price'>전고(Overall Height)</span><p style='font-size:15px;'>접지면에서 가장 높은 부분까지의 높이, 최대 적재 상태일 때는 해당 조건을 명시한다. 단, 막대식 안테나는 가장 낮춘 상태로 한다.<img width='200' src='/static/images/설명/전고.png'/></p>" });
	
  	$("#content3").html('<a id="공차중량" href="#a" title="">공차중량</a>');
  	$("#content3 #공차중량").tooltip({ content : "<span id='price'>공차중량(Unladen Vehicle Weight)</span><p style='font-size:15px;'>빈차 상태에서 중량으로 주행하는데 최소한의 장비를 지닌 자동차의 상태를 말하며, 규격 또는 법규에 따라 정의가 다르다.</p>" });
	
  	$("#content4").html('<a id="연료탱크용량" href="#a" title="">연료탱크 용량</a>');
  	$("#content4 #연료탱크용량").tooltip({ content : "<span id='price'>연료탱크 용량(Fuel Tank Capacity)</span><p style='font-size:15px;'>연료를 저장할 수 있는 양, 차종별 1일 소요량을 기준으로 하기 때문에 배기량이 높을수록 탱크 용량도 큰 경우가 많다.</p>" });
	
  	$("#content5").html('<a id="전폭" href="#a" title="">전폭</a>');
  	$("#content5 #전폭").tooltip({ content : "<span id='price'>전폭(Overall Width)</span><p style='font-size:15px;'>사이드 미러를 제외한 기본 부착물을 포함하여 수평에서 놓여진 자체의 좌우 끝단 사이의 너비를 말한다.<br><br><img width='200' src='/static/images/설명/전폭.png'/></p>" });
	
  	$("#content6").html('<a id="축거" href="#a" title="">축거</a>');
  	$("#content6 #축거").tooltip({ content : "<span id='price'>축거(Wheel Base)</span><p style='font-size:15px;'>앞뒤 차축의 중심에서 중심까지의 수평거리를 뜻한다. 차죽이 2개인 것은 앞 차축 사이를 제 1축거, 중간 및 뒷 차축 사이를 제 2축거라고 한다. 단, 좌우가 다르면 각각 표시<img width='200' src='/static/images/설명/축거.png'/></p>" });
	
  	$("#content7").html('<a id="승차정원" href="#a" title="">승차정원</a>');
  	$("#content7 #승차정원").tooltip({ content : "<span id='price'>승차정원(Limit Number)</span><p style='font-size:15px;'>차량의 실내에 승차할 수 있는 사람의 수를 뜻한다.</p>" });
	
  	$("#content8").html('<a id="트렁크용량" href="#a" title="">트렁크 용량</a>');
  	$("#content8 #트렁크용량").tooltip({ content : "<span id='price'>트렁크 용량(Trunk Capaticy)</span><p style='font-size:15px;'>물건을 넣어 두는 트렁크의 크기를 말한다.</p>" });
	
  	$("#content10").html('<a id="최고출력" href="#a" title="">최고출력</a>');
  	$("#content10 #최고출력").tooltip({ content : "<span id='price'>최고출력(Maximum Power)</span><p style='font-size:15px;'>엔진에서 발생될 수 있는 최대 동력. 최대마력이라고도 하며 1분당 엔진회전수(rpm)를 측정하여 최고 출력을 마력으로 표현한다.</p>" });
	
  	$("#content11").html('<a id="최대토크" href="#a" title="">최대토크</a>');
  	$("#content11 #최대토크").tooltip({ content : "<span id='price'>최대토크(Maximum Torque)</span><p style='font-size:15px;'>엔젠의 회전력이 가장  강할 때 힘으로 kg.m/rpm으로 표시하며, 최대 토크 부근의 회전력이 가장 달리기 좋은 포인트가 된다. 토크 폭이 넓은 엔진이 사용하기 쉽다고 생각하지만 출력이 낮아진다.</p>" });
	
  	$("#content12").html('<a id="엔진위치" href="#a" title="">엔진위치</a>');
  	$("#content12 #엔진위치").tooltip({ content : "<span id='price'>엔진위치(Engine Position)</span><p style='font-size:15px;'>FF(Front Front)는 엔진위치가 앞이며 구동축이 앞바퀴란 뜻이다. FR(Front Real)은 앞에 엔진, 구동축은 뒤에 위치한다. RR은 엔진과 구동이 전부 뒷바퀴쪽에 있다는 뜻이다.<img width='200' src='/static/images/설명/엔진위치.png'/></p>" });
	
  	$("#content14").html('<a id="배기량" href="#a" title="">배기량</a>');
  	$("#content14 #배기량").tooltip({ content : "<span id='price'>배기량(Displacement)</span><p style='font-size:15px;'>피스톤이 실린더 내에서 1행정 할때 흡입이나 배출한 공기 또는 혼합 가스의 체적을 말한다. 각 기통의 실린더 x 스트로크 x 기통수로 나타낸다. 배기량은 엔진 크기의 척도로 차 자체의 급수를 나타내기도 한다.<img width='200' src='/static/images/설명/배기량.png'/></p>" });
	
  	$("#content17").html('<a id="최고속도" href="#a" title="">최고속도</a>');
  	$("#content17 #최고속도").tooltip({ content : "<span id='price'>최고속도(Maximum Speed)</span><p style='font-size:15px;'>자동차가 주행할 수 있는 최고로 높은 한계치의 속도</p>" });
	
  	$("#content19").html('<a id="구동방식" href="#a" title="">구동방식</a>');
  	$("#content19 #구동방식").tooltip({ 
  		content : "<span id='price'>구동방식(Drive Type)</span><p style='font-size:12px;'>전륜구동(FF)은 설계가 쉽고 엔진과 구동축이 앞에 있어 눈길에 좋다. 그러나 높은 속도, 급제동 시 안정감이 떨어진다.<br><br>" + 
  		"후륜구동(FR)은 엔진은 앞에 구동축은 뒤에 있는 형태다. 실내공간은 좁아지고 난이도 높은 설계로 단가가 높아진다.<br><br>" + 
  		"미드쉽 후륜구동(MR)은 엔진이 차제 중앙에 위치하며 엔진의 무게가 차량의 중심을 잡아 무게 분배가 안정적. 반면 설계의 한계로 승차인원이 적어진다는 단점이 있다.<br><br>" + 
  		"상시 사륜구동(AWD)은 풀타임 사륜구동이라고도 하며, 바퀴 모두 작동하는 타입이다.<br><br>" +
  		"일시 사륜구동(4WD)은 파트타임 사륜구동이라고 하며, 운전자의 조작에 따라 앞바퀴 또는 뒷바퀴만 구동, 필요시 사륜을 사용한다.<br><br>" +
  		"리어 후륜구동(RR)은 차체 뒤쪽에 장착되고 뒷바퀴 차축의 힘을 이용해서 작동하는 방식이다." +
  		"<img width='190' src='/static/images/설명/구동방식.png'/><p>"  		
  	});
	
  	$("#content20").html('<a id="파워스티어링" href="#a" title="">파워스트어링</a>');
  	$("#content20 #파워스티어링").tooltip({ content : "<span id='price'>파워스티어링(Power Stearing)</span><p style='font-size:15px;'>자동차에서 동력에 따른 조향장치. 유압, 공기압으로 핸들 조작을 쉽게 해준다.<img width='200' src='/static/images/설명/파워스티어링.png'/></p>" });
  	
  	$("#content22").html('<a id="전륜타이어크기" href="#a" title="">전륜 타이어 크기</a>');
  	$("#content22 #전륜타이어크기").tooltip({ content : "<span id='price'>타이어 규격(Tire Size)</span><p style='font-size:15px;'><br>타이어 제조사 마다 표시 방법이 다르지만 예시로 175/60R13이라고 하면 의미는 다음과 같다.<br><br>175 : 타이어 단면 폭<br>60 : 편평비. 타이어의 단면 높이<br>래디얼(Radial) 타이어<br>13 : 림 외경<br>" + 
  	"<img width='200' src='/static/images/설명/타이어.png'/></p>" });
  	
  	$("#content23").html('<a id="전륜서스펜션" href="#a" title="">전륜 서스펜션</a>');
  	$("#content23 #전륜서스펜션").tooltip({ content : "<span id='price'>서스펜션(Suspention)</span><p style='font-size:15px;'>현가장치라고도 하며 쇼크업소버, 스프링, 서스펜션암이 주요 구성이다. 노면에서 발생하는 충격을 흡수하는 역할을 한다.<img width='200' src='/static/images/설명/서스펜션.png'/></p>" });
  	
  	$("#content24").html('<a id="변속기" href="#a" title="">변속기</a>');
  	$("#content24 #변속기").tooltip({ content : "<span id='price'>변속기 기어 단수(Transmission)</span><p style='font-size:15px;'>변소기란, 클러치와 구동축(Drive Shaft) 또는 클러치와 종감속 기어 장치 사이에 설치되어 자동차 주행 상태에 맞도록 회전력과 속도를 바꾸어 구동 바퀴에 전달하는 역할을 하는 기계장치이다." + 
  	"<br>종류로는 (수동, 자동, 무단 변속기) 등이 있다.<br><img width='200' src='/static/images/설명/변속기.png'/></p>" });
  	
  	$("#content25").html('<a id="스티어링" href="#a" title="">스티어링</a>');
  	$("#content25 #스티어링").tooltip({ content : "<span id='price'>스티어링(Steering)</span><p style='font-size:15px;'>자동차가 진행방향을 바꾸기 위해 앞바퀴와 회전축 방향을 바꾸는 장치.<img width='200' src='/static/images/설명/스티어링.png'/></p>" });
	
  	$("#content27").html('<a id="후륜타이어크기" href="#a" title="">후륜 타이어 크기</a>');
  	$("#content27 #후륜타이어크기").tooltip({ content : "<span id='price'>타이어 규격(Tire Size)</span><p style='font-size:15px;'><br>타이어 제조사 마다 표시 방법이 다르지만 예시로 175/60R13이라고 하면 의미는 다음과 같다.<br><br>175 : 타이어 단면 폭<br>60 : 편평비. 타이어의 단면 높이<br>래디얼(Radial) 타이어<br>13 : 림 외경<br>" + 
  	"<img width='200' src='/static/images/설명/타이어.png'/></p>" });
  	
  	$("#content28").html('<a id="후륜서스펜션" href="#a" title="">후륜 서스펜션</a>');
  	$("#content28 #후륜서스펜션").tooltip({ content : "<span id='price'>서스펜션(Suspention)</span><p style='font-size:15px;'>현가장치라고도 하며 쇼크업소버, 스프링, 서스펜션암이 주요 구성이다. 노면에서 발생하는 충격을 흡수하는 역할을 한다.<img width='200' src='/static/images/설명/서스펜션.png'/></p>" });
  	
  	$("#content29").html('<a id="연료" href="#a" title="">연료</a>');
  	$("#content29 #연료").tooltip({ content : "<span id='price'>연료(Fuel)</span><p style='font-size:15px;'>엔진에 공급되어 연소 가능한 물질로 가솔린 엔진에는 휘발류<br>" + 
  	"디젤엔진에는 경유, LPG에는 LPG 연료가 사용된다. 엔진에서 연소되어 연소열이 연소가스를 팽창시켜 피스톤을 아래로 밀어 내어 크랭크 축을 돌리게 된다.</p>" });
	
  	$("#content30").html('<a id="연비" href="#a" title="">연비</a>');
  	$("#content30 #연비").tooltip({ content : "<span id='price'>연비(Fuel Consumption Ratio)</span><p style='font-size:15px;'>자동차의 주행에 따라 소비되는 연료의 양<br><br>" + 
  	"주행거리를 사용한 연료의 양으로 나누어 연료 1리터당 주행 킬로미터로 표시한다.<br>" + 
  	"예를 들어 100km를 주행하는데 소모된 연료가 14ℓ였다면 연비는 100km / 14ℓ = 7.14km/ℓ가 된다.</p>" });
	
  	$("#content32").html('<a id="이산화탄소" href="#a" title="">이산화탄소 배출량</a>');
  	$("#content32 #이산화탄소").tooltip({ content : "<span id='price'>이산화탄소 배출량(Carbon Dioxide Emission)</span><p style='font-size:15px;'>자동차의 주행에 따라 배출되는 이산화탄소의 양.<br>" + 
  	"1km당 배출되는 이산화탄소의 양으로 표준 연비 측정을 위한 모의주행시 생성된 배기가스를 포집하여, 분석장치를 통해 측정한 실측값이다.</p>" });
	
  	$("#content33").html('<a id="연비등급" href="#a" title="">연비등급</a>');
  	$("#content33 #연비등급").tooltip({ content : "<span id='price'>연비등급(Fuel Economy Ratings)</span><p style='font-size:15px;'>자동차의 연비 효율성을 나타내는 에너지 소비효율 등급 표시방법<br><br>" + 
  	"차량의 배기량에 따라 승용차는 8개군, 다목적형 차량은 3개군으로 분류되며 각 군별로 5개 등급으로 분류되어 연비등급으로 표시한다.</p>" });
	
	});