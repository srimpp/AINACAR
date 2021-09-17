function sortTD(n){
	let table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
	table = document.getElementById("member_list");
	switching = true;
	dir = "asc";
	
	while (switching){
		switching = false;
		rows= table.rows;
		for (i=1;i<(rows.length-1);i++){
			shouldSwitch=false;
			x= rows[i].getElementByTagName("TD")[n];
			y= rows[i+1].getElementByTagName("TD")[n];
			if(dir=="asc"){
				if(x.innerHTML.toLowerCase()>y.innerHTML.toLowerCase()){
					shouldSwitch = true;
					break;
				}
			} else if (dir == "desc"){
				if(x.innerHTML.toLowerCase()<y.innerHTML.toLowerCase()){
					shouldSwitch = true;
					break;
				}
			}
		}
		if (shouldSwitch){
			rows[i].parentNode.insertBefore(rows[i+1],rows[i]);
			switching=true;
			switchcount ++;
		} else{
			if (switchcount==0 && dir == "asc"){
				dir = "desc";
				switching =true;
			}	
		}
	}
}

/*
function reverseTD(n){
	replace.descending(index);
}
*/