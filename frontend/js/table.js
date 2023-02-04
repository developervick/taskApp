

function rows(numRows) {
		
    /* To create no. of rows of table and returns the node List of
    <tr> element equal to the length of numRows */
    var num = numRows
    
    var rows = []
    for( var i=0; i<num; i++){
        let row = document.createElement('tr')
            row.id = 'row' + i
            rows.push(row)
    }	
    return rows
}


function cols(numCols) {
    /* To create cells of table and returns nodeList of <td> 
        element equal to the length of numCols */
    
    let num = numCols
    var cols = []
    for( let i=0; i<numCols; i++){
    let col = document.createElement('td')
        col.id = 'col' + i
        col.innerHTML = 'cell'+i
        cols.push(col)
    }
    
    return cols
}


function table(numCols, numRows,tableId, insideHTML) {
    /* Returns a table of dimentions passed 
    parameters are
    numCols, numRows are integers
    insideHTML is array of elements equal to the length of no. of cells
    */

    var cellNo = 0
    var count = -1

    let table = document.querySelector(tableId)
    console.log(table)
    
    rows(numRows).forEach((row)=>{
        table.appendChild(row)
    })

    let tableRows = table.childNodes
    
    for(i=1; i<tableRows.length; i++){
        count+
        cols(numCols).forEach((col)=>{
            count++
            col.id = 'cell '+count
            col.innerHTML = insideHTML[count]
            tableRows[i].appendChild(col)
        })	
    }
}