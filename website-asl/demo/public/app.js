document.addEventListener('DOMContentLoaded', function () {
    var darkmodeInstance = new Darkmode();
    darkmodeInstance.showWidget();
    isMorse = false;
    // Function to check dark mode status
    function checkDarkMode() {
        var isDarkModeActivated = darkmodeInstance.isActivated();

        if (isDarkModeActivated) {
            document.getElementById("dd").style.display = 'none';
            var typed = new Typed('#element', {
                strings: ['beep boop zeep zorp bloop'],
                typeSpeed: 50,
            });

            // Convert all <p> tags to Morse code
            var pTags = document.getElementsByTagName('p');
            for (var i = 0; i < pTags.length; i++) {
                pTags[i].innerHTML = convertToMorseCode(pTags[i].innerHTML);
            }

            // Convert all <h2> tags to Morse code
            var h2Tags = document.getElementsByTagName('h2');
            for (var i = 0; i < h2Tags.length; i++) {
                h2Tags[i].innerHTML = convertToMorseCode(h2Tags[i].innerHTML);
            }
            document.getElementById("cta-button").innerHTML = "Decrypt";
            document.getElementById("form").action = "/alien";      
            document.getElementById("subhead").innerHTML = "<p>Convert Alien sign language (ASL) into English!</p>"
            
        } else{
            // If not in dark mode, reset to original text
            document.getElementById("dd").style.display = '';
            
            var typed = new Typed('#element', {
                strings: ['<i>Hello</i> Human.', 'Welcome to The Future!'],
                typeSpeed: 50,
            });

            // Reset all <p> tags to original text
            if(isMorse){
            var pTags = document.getElementsByTagName('p');
            for (var i = 0; i < pTags.length; i++) {
                pTags[i].innerHTML = convertToValidMorseLowercase(pTags[i].innerHTML);
            }

            // Reset all <h2> tags to original text
            var h2Tags = document.getElementsByTagName('h2');
            for (var i = 0; i < h2Tags.length; i++) {
                h2Tags[i].innerHTML = convertToValidMorseLowercase(h2Tags[i].innerHTML);
            }
        }
        document.getElementById("cta-button").innerHTML = "Get Started";
        document.getElementById("form").action = "/run";  
        document.getElementById("subhead").innerHTML = "<p>Good communication is the bridge between confusion and clarity</p>"
        }

        return isDarkModeActivated;
    }

    // Check dark mode initially
    var isDarkModeActivatedInitially = checkDarkMode();

    // Check dark mode when the widget button is clicked
    var darkmodeToggle = document.querySelector('.darkmode-toggle');
    if (darkmodeToggle) {
        darkmodeToggle.addEventListener('click', checkDarkMode);
    }
    
particlesJS("particles-js", {
    particles: {
        number: {
            value: 100,
            density: {
                enable: true,
                value_area: 800
            }
        },
        color: {
            value: "#000" // Particle color (black)
        },
        shape: {
            type: "circle", // Particle shape
            stroke: {
                width: 0,
                color: "#000"
            },
            polygon: {
                nb_sides: 5
            }
        },
        opacity: {
            value: 0.5,
            random: false,
            anim: {
                enable: false,
                speed: 1,
                opacity_min: 0.1,
                sync: false
            }
        },
        size: {
            value: 3,
            random: true,
            anim: {
                enable: false,
                speed: 40,
                size_min: 0.1,
                sync: false
            }
        },
        line_linked: {
            enable: true,
            distance: 150,
            color: "#000",
            opacity: 0.4,
            width: 1
        },
        move: {
            enable: true,
            speed: 6,
            direction: "none",
            random: false,
            straight: false,
            out_mode: "out",
            bounce: false,
            attract: {
                enable: false,
                rotateX: 600,
                rotateY: 1200
            }
        }
    },
    interactivity: {
        detect_on: "canvas",
        events: {
            onhover: {
                enable: true,
                mode: "grab"
            },
            onclick: {
                enable: true,
                mode: "push"
            },
            resize: true
        },
        modes: {
            grab: {
                distance: 140,
                line_linked: {
                    opacity: 1
                }
            },
            bubble: {
                distance: 400,
                size: 40,
                duration: 2,
                opacity: 8,
                speed: 3
            },
            repulse: {
                distance: 200,
                duration: 0.4
            },
            push: {
                particles_nb: 4
            },
            remove: {
                particles_nb: 2
            }
        }
    },
    retina_detect: true
});

document.getElementById("particles-js").style.zIndex = "-2";

function runPython() {
    console.log("hello!")
}

document.getElementById("cta-button").addEventListener("click", function() {
    runPython();
});

});



function convertToMorseCode(str) {
    isMorse = true;
    const morseCodeMap = {
        A: ".-",
        B: "-...",
        C: "-.-.",
        D: "-..",
        E: ".",
        F: "..-.",
        G: "--.",
        H: "....",
        I: "..",
        J: ".---",
        K: "-.-",
        L: ".-..",
        M: "--",
        N: "-.",
        O: "---",
        P: ".--.",
        Q: "--.-",
        R: ".-.",
        S: "...",
        T: "-",
        U: "..-",
        V: "...-",
        W: ".--",
        X: "-..-",
        Y: "-.--",
        Z: "--..",
        " ": "/",
    };

    const morseCodeArr = [];
    const upperCaseStr = str.toUpperCase();

    for (let i = 0; i < upperCaseStr.length; i++) {
        const char = upperCaseStr[i];
        const morseCode = morseCodeMap[char];

        if (morseCode) {
            morseCodeArr.push(morseCode);
        }
    }

    return morseCodeArr.join(" ");
}

function convertToValidMorseLowercase(morseCode) {
    isMorse = false;
    const validMorseCodeMap = {
        ".-": "a",
        "-...": "b",
        "-.-.": "c",
        "-..": "d",
        ".": "e",
        "..-.": "f",
        "--.": "g",
        "....": "h",
        "..": "i",
        ".---": "j",
        "-.-": "k",
        ".-..": "l",
        "--": "m",
        "-.": "n",
        "---": "o",
        ".--.": "p",
        "--.-": "q",
        ".-.": "r",
        "...": "s",
        "-": "t",
        "..-": "u",
        "...-": "v",
        ".--": "w",
        "-..-": "x",
        "-.--": "y",
        "--..": "z",
        "/": " ",
    };

    const morseCodeArr = morseCode.split(" ");
    const validStrArr = [];

    for (let i = 0; i < morseCodeArr.length; i++) {
        const code = morseCodeArr[i];
        const validChar = validMorseCodeMap[code];

        if (validChar) {
            validStrArr.push(validChar);
        }
    }

    return validStrArr.join("");
}
