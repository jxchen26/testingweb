//when the page is loaded it checks for how many forms there are suppose to be on the page. 
window.addEventListener('load', function () {
	let all_btns = document.getElementsByClassName("form-btn")
	for (let btn of all_btns){
		btn.addEventListener("click",function(){deleteFormEntry(btn)})
	}
})


function deleteFormEntry(btn){
	// var f = sessionStorage.getItem("moreforms")
	// f = parseInt(f) - 1
	// sessionStorage.setItem("moreforms",f)
	
	btn.parentNode.remove()
}