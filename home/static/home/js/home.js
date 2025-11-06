function toggleMenu() {
            const menu = document.getElementById('navMenu');
            const hamburger = document.querySelector('.hamburger');
            menu.classList.toggle('active');
            hamburger.classList.toggle('active');
        }

        // Cerrar menú al hacer clic en un enlace (mobile)
        document.querySelectorAll('.nav-link, .btn').forEach(link => {
            link.addEventListener('click', () => {
                if (window.innerWidth <= 768) {
                    const menu = document.getElementById('navMenu');
                    const hamburger = document.querySelector('.hamburger');
                    menu.classList.remove('active');
                    hamburger.classList.remove('active');
                }
            });
        });


document.getElementById('searchCategory').addEventListener('change', function() {
    const value = this.value;
    const url_all = this.dataset.allServices;
    if (value === 'all') {
        // redirige al home (todas las categorías)
        window.location.href = url_all;
    } else {
        // redirige a la categoría seleccionada
        window.location.href = value;
    }
});

