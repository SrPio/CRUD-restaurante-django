(function () {
    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm("¿Deseas eliminar el plato?");
            if (!confirmacion) {
                e.preventDefault();
            }
        })
    })
})();