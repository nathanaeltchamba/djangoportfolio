let theme = localStorage.getItem('theme')

if (theme == null) {
    setTheme('green')
} else {
    setTheme(theme)
}

let themeDots = document.getElementsByClassName('theme-dot')

for (var i = 0; themeDots.length > i; i++) {
    themeDots[i].addEventListener('click', function () {
        let mode = this.dataset.mode
        console.log('Option clicked:', mode)
        setTheme(mode)
    })
} 

function setTheme(mode) {
    if (mode == 'light') {
        document.getElementById('theme-styled').href = static + '/main.css'
    }

    if (mode == 'blue') {
        document.getElementById('theme-styled').href = static + '/blue.css'
    }

    if (mode == 'green') {
        document.getElementById('theme-styled').href = static + '/green.css'
    }

    if (mode == 'purple') {
        document.getElementById('theme-styled').href = static + '/purple.css'
    }

    localStorage.setItem('theme', mode)
}

document.querySelectorAll('a[href^="#"]').forEach(anchor =>{
    anchor.addEventListener("click", function(e){
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth"
        })
    })
})