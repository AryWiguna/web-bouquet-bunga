/* ============================================
   🌸 ANIMATED FLOWER BOUQUET — SCRIPT
   Fireflies and Animation Trigger
   ============================================ */

(function () {
    'use strict';

    /* ==========================================
       FIREFLY PARTICLE SYSTEM (Canvas)
       ========================================== */
    const canvas = document.getElementById('fireflies-canvas');
    const ctx = canvas.getContext('2d');
    let fireflies = [];
    let canvasWidth, canvasHeight;
    let fireflyCount = 40;

    function resizeCanvas() {
        canvasWidth = window.innerWidth;
        canvasHeight = window.innerHeight;
        canvas.width = canvasWidth;
        canvas.height = canvasHeight;

        if (canvasWidth < 480) {
            fireflyCount = 25;
        } else if (canvasWidth < 768) {
            fireflyCount = 30;
        } else if (canvasWidth < 1024) {
            fireflyCount = 35;
        } else {
            fireflyCount = 45;
        }
    }

    class Firefly {
        constructor() {
            this.reset();
        }

        reset() {
            this.x = Math.random() * canvasWidth;
            this.y = Math.random() * canvasHeight;
            this.size = 1.5 + Math.random() * 3;
            this.baseSize = this.size;
            this.speedX = (Math.random() - 0.5) * 0.6;
            this.speedY = (Math.random() - 0.5) * 0.6;

            this.opacity = 0.2 + Math.random() * 0.6;
            this.glowPhase = Math.random() * Math.PI * 2;
            this.glowSpeed = 0.01 + Math.random() * 0.03;
            this.maxOpacity = 0.5 + Math.random() * 0.5;
            this.minOpacity = 0.05 + Math.random() * 0.15;

            this.wobblePhase = Math.random() * Math.PI * 2;
            this.wobbleSpeed = 0.005 + Math.random() * 0.015;
            this.wobbleAmplitude = 0.3 + Math.random() * 0.8;

            const hue = 38 + Math.random() * 20; 
            const saturation = 80 + Math.random() * 20;
            const lightness = 60 + Math.random() * 25;
            this.color = `hsl(${hue}, ${saturation}%, ${lightness}%)`;
            this.glowColor = `hsla(${hue}, ${saturation}%, ${lightness + 10}%, `;
        }

        update() {
            this.wobblePhase += this.wobbleSpeed;
            this.x += this.speedX + Math.sin(this.wobblePhase) * this.wobbleAmplitude * 0.3;
            this.y += this.speedY + Math.cos(this.wobblePhase * 0.7) * this.wobbleAmplitude * 0.2;

            this.glowPhase += this.glowSpeed;
            this.opacity = this.minOpacity + (this.maxOpacity - this.minOpacity) *
                (0.5 + 0.5 * Math.sin(this.glowPhase));

            this.size = this.baseSize * (0.8 + 0.4 * Math.sin(this.glowPhase * 0.8));

            const margin = 50;
            if (this.x < -margin) this.x = canvasWidth + margin;
            if (this.x > canvasWidth + margin) this.x = -margin;
            if (this.y < -margin) this.y = canvasHeight + margin;
            if (this.y > canvasHeight + margin) this.y = -margin;
        }

        draw() {
            ctx.save();
            const glowRadius = this.size * 8;
            const gradient = ctx.createRadialGradient(
                this.x, this.y, 0,
                this.x, this.y, glowRadius
            );
            gradient.addColorStop(0, this.glowColor + (this.opacity * 0.6) + ')');
            gradient.addColorStop(0.3, this.glowColor + (this.opacity * 0.2) + ')');
            gradient.addColorStop(1, this.glowColor + '0)');

            ctx.fillStyle = gradient;
            ctx.beginPath();
            ctx.arc(this.x, this.y, glowRadius, 0, Math.PI * 2);
            ctx.fill();

            ctx.globalAlpha = this.opacity;
            ctx.fillStyle = this.color;
            ctx.shadowBlur = this.size * 6;
            ctx.shadowColor = this.color;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();

            ctx.globalAlpha = Math.min(1, this.opacity * 1.5);
            ctx.fillStyle = '#fffde7';
            ctx.shadowBlur = this.size * 3;
            ctx.shadowColor = '#fff9c4';
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size * 0.4, 0, Math.PI * 2);
            ctx.fill();
            ctx.restore();
        }
    }

    function initFireflies() {
        fireflies = [];
        for (let i = 0; i < fireflyCount; i++) {
            fireflies.push(new Firefly());
        }
    }

    function animateFireflies() {
        ctx.clearRect(0, 0, canvasWidth, canvasHeight);
        for (const fly of fireflies) {
            fly.update();
            fly.draw();
        }
        requestAnimationFrame(animateFireflies);
    }

    resizeCanvas();
    initFireflies();
    animateFireflies();

    let resizeTimeout;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(() => {
            resizeCanvas();
            while (fireflies.length < fireflyCount) {
                fireflies.push(new Firefly());
            }
            while (fireflies.length > fireflyCount) {
                fireflies.pop();
            }
        }, 200);
    });


    /* ==========================================
       ANIMATION TRIGGER
       ========================================== */
    window.onload = () => {
        // Remove not-loaded class to trigger CSS animations (like the github reference)
        setTimeout(() => {
            document.body.classList.remove("not-loaded");
            
            // Show wrapper, ribbon, and message manually based on overall animation timing
            setTimeout(() => {
                document.getElementById('wrapper').classList.add('visible');
            }, 300);

            setTimeout(() => {
                document.getElementById('ribbon').classList.add('visible');
            }, 800);
            
            setTimeout(() => {
                document.getElementById('message-section').classList.add('visible');
            }, 6000); // 6s wait to let flowers finish blooming

        }, 500);

        // Musik latar
    const music = document.getElementById('background-music');
    
    // Fungsi untuk memutar musik
    function playMusic() {
        music.play().catch(error => console.log("Autoplay dicegah oleh browser"));
        // Hapus listener setelah diklik agar tidak menumpuk
        document.removeEventListener('click', playMusic);
    }

    // Tunggu interaksi user (klik di mana saja) untuk mulai musik
    document.addEventListener('click', playMusic);

    if (localStorage.getItem('musicAllowed') === 'true') {
        music.play().catch(() => {
            console.log("Browser tetap memblokir autoplay setelah refresh.");
        });
    }
    };
    const splash = document.getElementById('splash-screen');
const music = document.getElementById('background-music');

function startExperience() {
    // 1. Mainkan musik
    music.play();
    
    // 2. Hilangkan layar splash
    splash.style.display = 'none';
    
    // 3. Tampilkan bouquet (jika kamu menyembunyikannya)
    // document.body.classList.remove("not-loaded"); 
    
    document.removeEventListener('click', startExperience);
}

splash.addEventListener('click', startExperience);

})();
