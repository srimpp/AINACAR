window.onload = function(){
	document.getElementById("btnIdOk").onclick = IdChk;
	document.getElementById("btnSignUp").onclick = SignChk;
	document.getElementById("btnCan").onclick = CanChk;
}


// id 중복확인
function IdChk(){
	if(NewMemForm.username.value == ""){
		alert('아이디를 입력하세요');
		NewMemForm.username.focus();
		return;
	};
	let regExp_id = /^[A-Za-z0-9가-힁]{4,}$/;
	if(!NewMemForm.username.value.match(regExp_id) ) {
		alert('아이디를 정확하게 입력하세요');
		NewMemForm.username.focus();
		return;
	};
	url = '/members/idcheck?username='+NewMemForm.username.value;
	window.open(url, 'username', "toolbar=no, width=300, height=150, top=200, left=300");
}

// 회원가입 정보 입력
function SignChk(){
	//alert('456');

	if(NewMemForm.password.value == ""){
		alert('비밀번호를 입력하세요');
		NewMemForm.password.focus();
		return;
	};
	let regExp_pass = /^[A-Za-z0-9]{6,12}$/;
	if(!NewMemForm.password.value.match(regExp_pass) ) {
		alert('비밀번호를 정확하게 입력하세요');
		NewMemForm.password.focus();
		return;
	};
	if(NewMemForm.password.value != NewMemForm.repassword.value){
		alert('비밀번호를 다시 확인해주세요');
		NewMemForm.repassword.focus();
		return;
	};
	if(NewMemForm.email.value == ""){
		alert('이메일을 입력하세요');
		NewMemForm.email.focus();
		return;
	};
	let regExp_email = /[0-9a-zA-Z][_0-9a-zA-Z-]*@[_0-9a-zA-Z-]+(\.[_0-9a-zA-Z-]+){1,2}$/;
	if(!NewMemForm.email.value.match(regExp_email) ) {
		alert('이메일을 정확하게 입력하세요');
		NewMemForm.email.focus();
		return;
	};
	if(NewMemForm.full_name.value == ""){
		alert('이름을 입력하세요');
		NewMemForm.full_name.focus();
		return;
	};
	if(NewMemForm.username.value == ""){
		alert('전화번호를 입력하세요');
		NewMemForm.phone.focus();
		return;
	};
	let regExp_phone = /^\d{3}-\d{3,4}-\d{4}/; 
	if (!NewMemForm.phone.value.match(regExp_phone)) {
		alert('전화번호를 정확하게 입력하세요');
		NewMemFrom.phone.focus();
		return;
	};
	
	alert('회원가입이 완료되었습니다.')
	NewMemForm.submit();
}

function CanChk(){
	if(confirm('정말 취소하시겠습니까?')){
		window.location.href = '/members/main'
	}
	else{
		return;
	}
	
}



