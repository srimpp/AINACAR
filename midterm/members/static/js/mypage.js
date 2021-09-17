
window.onload = function(){
	
	
	document.getElementById("btnSub").onclick = SubChk;
	document.getElementById("btnCan").onclick = CanChk;
	
}

function SubChk(){
	if(accountFrm.up_passwd.value == ""){
		alert('비밀번호를 입력하세요');
		accountFrm.up_passwd.focus();
		return;
	};
	
	alert('수정되었습니다');
	accountFrm.submit();

}


function CanChk(){
	if(confirm('정말 취소하시겠습니까?')){
		window.location.href = '/members/login'
	}
	else{
		return;
	}
	
}
