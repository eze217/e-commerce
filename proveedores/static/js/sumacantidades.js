function suma_total() {
    //leo la tabla completa
    var resume_table = document.getElementById("rwd-table-id");
    var total_general = document.getElementById("totalGeneral")
    //recorro las filas
    totalgeneral = 0
    for (var i = 1, row; row = resume_table.rows[i]; i++) {
        cantidad = 0
        costo = 0
        total = 0

        //dentro de la fila recorro celda x celda
        for (var j = 0, col; col = row.cells[j]; j++) {

            // tomo de unicamente de la celda que necesito el dato
            if (j == 2) {
                cantidad = $($(col).children("input")[0]).val()
                if (cantidad === NaN || cantidad == 0) {
                    cantidad = 0
                }
            }
            if (j == 3) {
                costo = parseInt(col.innerText)
            }

            if (j == 4) {
                col.innerText = costo * cantidad
                totalgeneral += parseInt(col.innerText)
                
            }
        }
    }


    total_general.innerHTML = 'Total general:' + " " + totalgeneral + ' €'

}