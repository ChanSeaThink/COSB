    window.onload=function(){
    	var coderequest=document.getElementById("code_request");
    	var code=document.getElementById("code");
    	coderequest.onclick=function(){
      	code.src="/getCAPTCHA/?nocache="+Math.random();
    	}
  	}