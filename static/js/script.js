document.addEventListener("DOMContentLoaded", function () {
    console.log("Tizim yuklandi ✅");

    // Animate all .animate-up elements
    const animated = document.querySelectorAll(".animate-up");
    animated.forEach(el => {
        el.style.opacity = 0;
        setTimeout(() => {
            el.classList.add("animate-up");
            el.style.opacity = 1;
        }, 100);
    });

    // Confirm delete alert
    const deleteForms = document.querySelectorAll("form[action*='delete']");
    deleteForms.forEach(form => {
        form.addEventListener("submit", function (e) {
            const confirmed = confirm("Siz ushbu korxonani o‘chirib tashlamoqchimisiz?");
            if (!confirmed) {
                e.preventDefault();
            }
        });
    });
});
