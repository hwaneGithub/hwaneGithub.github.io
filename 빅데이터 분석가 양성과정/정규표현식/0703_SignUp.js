

// ID, PW, E-mail 유효성 검사 함수
function validity() {
    
/*  ID, PW, E-mail 유효성 검사 정규표현식
    ID => var 변수명=/^[a-zA-Z0-9]{4,12}$/;
    PW => var 변수명=/^(?=.*[a-zA-Z])((?=.*\d)|(?=.*\W)).{6,20}$/;
    E-mail => var 변수명=/^[a-z0-9_+.-]+@([a-z0-9]+\.)+[a-z0-9]{2,4}$/;
*/
    var check_IdPw = /^[a-zA-Z0-9]{4,12}$/
    var check_email = /^[a-zA-Z0-9]([-_.]?[a-zA-Z0-9])+@[a-zA-Z0-9]([-_.]?[a-zA-Z0-9])*.[a-zA-Z]{2,3}$/i;

    var id = document.getElementById("id");                                          // ID값으로 호출
    var pw = document.getElementById("pw");
    var email = document.getElementById("email");
    var num1 = document.getElementById("num1");
    var num2 = document.getElementById("num2");

    var arrNum1 = new Array();                                                       // 주민번호 앞자리숫자 6개를 담을 배열
    var arrNum2 = new Array();                                                       // 주민번호 뒷자리숫자 7개를 담을 배열

// 아이디, 비번 미입력시 alert로 입력 요청 안내창 뜨고, focus() 함수로 해당 입력란에 커서를 위치시킴
    if(id.value == "") {
        alert("아이디를 입력해 주세요");
        id.focus();
        return false;
    }
// !function() : 함수가 반환하는 것의 반대 값 반환
    if(!checkIP(check_IdPw,id,"아이디는 4~12자의 영문 대/소문자, 숫자로만 입력해주세요.")) {
        return false;
    }

    if(pw.value == "") {
        alert("비밀번호를 입력해주세요.");
        pw.focus();
        return false;
    }
    if(!checkIP(check_IdPw,pw,"비밀번호는 4~12자의 영문 대/소문자, 숫자로만 입력해주세요.")) {
        return false;
    }

// 비밀번호 값와 비밀번호 확인 값 비교 signUp(form의 이름).pw(id가 pw인) )
    if(signUp.pw.value != signUp.checkpw.value) {
        alert("비밀번호를 다시 확인해주세요.");
// signUp.checkpw.value를 초기화하고, .focus()로 signUp.checkpw에 커서 부여
        signUp.checkpw.value = "";
        signUp.checkpw.focus();
        return false;
    }

    if(email.value=="") {
        alert("이메일을 입력해 주세요");
        email.focus();
        return false;
    }
    if(!checkE(check_email, email, "적합하지 않은 이메일 형식입니다.")) {
        return false;
    }

    if(signUp.name.value=="") {
        alert("이름을 입력해 주세요");
        signUp.name.focus();
        return false;
    }

// 반복문으로 주민번호 앞자리, 뒷자리를 각각의 배열에 순서대로 넣음.
    for (var i=0; i<num1.value.length; i++) {
        arrNum1[i] = num1.value.charAt(i);
    }
    for (var i=0; i<num2.value.length; i++) {
        arrNum2[i] = num2.value.charAt(i);
    }
// 주민번호 더하는 변수
    var tempSum=0;
/* 
    주민번호 검사방법을 적용해 앞 번호를 모두 계산하여 더함
    1~6번째 자리까지 각각 2~7을 곱하므로 각 배열값에 2+i을 곱하고 곱한 값을 다 더함 2093430
*/
    for (var i=0; i<num1.value.length; i++) {
        tempSum += arrNum1[i] * (2+i);
    }
/*
    앞 번호들의 계산 결과에 뒷번호 계산 결과를 모두 더함.(단, 마지막 7번째는 계산에 포함하지 않으므로 길이에서 -1만큼 반복)
    3~6번째 자리는 각각 2~5를 곱하므로 각 배열값에 i를 곱하고,
    1,2번째 자리는 8,9를 곱하므로 각 배열값에 8+i을 곱함
*/
    for (var i=0; i<num2.value.length-1; i++) {
        if(i>=2) {
            tempSum += arrNum2[i] * i;
        }
        else {
            tempSum += arrNum2[i] * (8+i);
        }
    }
/*
    11을 위 계산의 결과값(tempSum)을 11로 나눈 나머지로 빼서 나온 값의 일(1)의 자리와
    주민번호 마지막 값을 비교해서 다르면 올바르지 않은 번호라고 알리고, 맞으면 생일 자동 등록 수행
    
    parseInt(): 문자열을 정수로 반환
    .substring(시작값, 끝값): 문자열 특정 부분만 추출할 때 사용하는 method => 주민번호 앞자리 연, 월, 일 구분
*/
    if((11-(tempSum%11))%10!=arrNum2[6]) {
        alert("올바른 주민번호가 아닙니다.");
        num2.value = "";
        num2.focus();
        return false;
    }else{
        if(arrNum2[0]==1 || arrNum2[0]==2) {
            var y = parseInt(num1.value.substring(0,2));
            var m = parseInt(num1.value.substring(2,4));
            var d = parseInt(num1.value.substring(4,6));
            signUp.year.value = 1900 + y;
            signUp.month.value = m;
            signUp.date.value = d;
        }
        else if(arrNum2[0]==3 || arrNum2[0]==4) {
            var y = parseInt(num1.value.substring(0,2));
            var m = parseInt(num1.value.substring(2,4));
            var d = parseInt(num1.value.substring(4,6));
            signUp.year.value == 2000 + y;
            signUp.month.value = m;
            signUp.date.value = d;
        }
    }

    // 관심분야, 자기소개 미입력시 하라는 메시지 출력
    if(signUp.interest[0].checked==false &&
        signUp.interest[1].checked==false &&
        signUp.interest[2].checked==false &&
        signUp.interest[3].checked==false &&
        signUp.interest[4].checked==false) {
        alert("관심분야를 골라주세요");
        return false;
    }
    if(signUp.my_intro.value=="") {
        alert("자기소개를 입력하세요");
        signUp.my_intro.focus();
        return false;
    }
    
    alert("회원가입이 완료되었습니다.");
}




//Id, Pw, E-mail 확인하는 함수
function checkIP(check_IdPw, column, message) {
    if(check_IdPw.test(column.value)) {
        return true;
    }
    alert(message);
    column.focus();
}
function checkE(check_email, column, message) {
    if(check_email.test(column.value)) {
        return true;
    }
    alert(message);
    column.focus();
}



// 우편번호
function postcode() {
     new daum.Postcode({
// 팝업에서 검색결과 항목 클릭 시 실행 코드 작성 부분
         oncomplete: function(data) {                    
                                                         // 각 주소의 노출 규칙에 따라 주소를 조합한다.
                                                         // 내려오는 변수가 값이 없는 경우엔 공백("")값을 가지므로, 이를 참고하여 분기 한다.
             var fullAddr = "";                          // 최종 주소 변수
             var extraAddr = "";                         // 조합형 주소 변수
                                                         // 사용자가 선택한 주소 타입에 따라 해당 주소 값을 가져온다.
             if (data.userSelectedType === "R") {        // 사용자가 도로명 주소를 선택했을 경우
                 fullAddr = data.roadAddress;
             } else {                                    // 사용자가 지번 주소를 선택했을 경우(J)
                 fullAddr = data.jibunAddress;
             }
                                                         // 사용자가 선택한 주소가 도로명 타입일때 조합한다.
             if(data.userSelectedType === "R"){
                 if(data.bname !== ""){                  //법정동명이 있을 경우 추가한다.
                     extraAddr += data.bname;
                 }
                 if(data.buildingName !== ""){           // 건물명이 있을 경우 추가한다.
                     extraAddr += (extraAddr !== "" ? ", " + data.buildingName : data.buildingName);
                 }
                 fullAddr += (extraAddr !== "" ? " ("+ extraAddr +")" : "");     // 조합형주소의 유무에 따라 양쪽에 괄호를 추가하여 최종 주소를 만든다.
             }
             document.getElementById("zip_code").value = data.zonecode;           // 우편번호와 주소 정보를 해당 필드에 넣는다.5자리 새우편번호 사용
             document.getElementById("main_address").value = fullAddr;
             document.getElementById("sub_address").focus();                     // 커서를 상세주소 필드로 이동한다.
         }
     }).open();
 }


// 음악 재생
function play() {
    var audio = document.getElementById("play_audio");
    if (audio.paused) { 
        audio.play(); 
    }
} 