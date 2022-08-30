$(document).ready(function() {
    $('.largecarousel').owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        // transform: 'translate3d(0px,0px,0px)',
        // transform: 'translate3d(' + coordinate + 'px,0px,0px)',
        responsive: {
            // 0: {
            //     items: 1
            // },
            // 600: {
            //     items: 3
            // },
            1000: {
                items: 1,
                // loop: false
            }
        }
    })
    $('.carousel2').owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        // transform: 'translate3d(0px,0px,0px)',
        // transform: 'translate3d(' + coordinate + 'px,0px,0px)',
        responsive: {
            // 0: {
            //     items: 1
            // },
            // 600: {
            //     items: 3
            // },
            1000: {
                items: 4,
                loop: false
            }
        }
    })
    $('.intercarousel').owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        dots: false,
        navText: ["<i class='fa fa-chevron-left'></i>", "<i class='fa fa-chevron-right'></i>"],
        responsive: {
            // 0: {
            //     items: 1
            // },
            // 600: {
            //     items: 3
            // },
            1000: {
                items: 1
            }
        }
    })
    $('.owl-carousel').owlCarousel({
        loop: true,
        margin: 10,
        nav: false,
        center: true,
        dots: false,
        responsive: {
            // 0: {
            //     items: 1
            // },
            // 600: {
            //     items: 3
            // },
            1000: {
                items: 3
            }
        }
    })
})