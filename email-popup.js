(function() {
    const EMAIL_ADDRESS = "ililoag@gmail.com";
    const emailButton = document.querySelector(".email-link");
    if (!emailButton) return;

    emailButton.setAttribute("href", `mailto:${EMAIL_ADDRESS}`);
    emailButton.setAttribute("role", "button");
    emailButton.setAttribute("aria-haspopup", "dialog");

    const style = document.createElement("style");
    style.textContent = `
        .email-popup-overlay {
            position: fixed;
            inset: 0;
            display: none;
            align-items: center;
            justify-content: center;
            background: rgba(0, 0, 0, 0.6);
            z-index: 2000;
            padding: 20px;
        }

        .email-popup-overlay.open {
            display: flex;
        }

        .email-popup {
            background: #0b0b0b;
            color: #f5f5f5;
            border: 1px solid #222;
            border-radius: 10px;
            width: 320px;
            max-width: 100%;
            padding: 22px 20px 18px;
            position: relative;
            box-shadow: 0 18px 40px rgba(0, 0, 0, 0.5);
        }

        .email-popup h3 {
            margin: 0 0 12px;
            font-size: 1.05rem;
            letter-spacing: 1px;
            text-transform: uppercase;
        }

        .email-popup .email-line {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
        }

        .email-popup .email-address {
            font-size: 0.95rem;
            color: #e8e8e8;
            word-break: break-all;
        }

        .email-popup .copy-btn {
            background: #fff;
            color: #000;
            border: none;
            padding: 10px 14px;
            border-radius: 6px;
            cursor: pointer;
            font-weight: 700;
            letter-spacing: 1px;
            min-width: 90px;
        }

        .email-popup .copy-btn:active {
            transform: translateY(1px);
        }

        .email-popup .close-btn {
            background: none;
            border: none;
            color: #888;
            position: absolute;
            top: 8px;
            right: 10px;
            font-size: 20px;
            cursor: pointer;
        }

        @media (max-width: 480px) {
            .email-popup {
                width: 100%;
            }
        }
    `;
    document.head.appendChild(style);

    const overlay = document.createElement("div");
    overlay.className = "email-popup-overlay";
    overlay.innerHTML = `
        <div class="email-popup" role="dialog" aria-modal="true" aria-label="Email contact">
            <button class="close-btn" aria-label="Close">×</button>
            <h3>Email</h3>
            <div class="email-line">
                <span class="email-address">${EMAIL_ADDRESS}</span>
                <button type="button" class="copy-btn">Copy</button>
            </div>
        </div>
    `;
    document.body.appendChild(overlay);

    const popup = overlay.querySelector(".email-popup");
    const copyBtn = overlay.querySelector(".copy-btn");
    const closeBtn = overlay.querySelector(".close-btn");
    const emailText = overlay.querySelector(".email-address");

    function openPopup() {
        overlay.classList.add("open");
        copyBtn.textContent = "Copy";
        copyBtn.disabled = false;
        copyBtn.focus();
    }

    function closePopup() {
        overlay.classList.remove("open");
        emailButton.focus();
    }

    emailButton.addEventListener("click", (evt) => {
        evt.preventDefault();
        openPopup();
    });

    closeBtn.addEventListener("click", closePopup);
    overlay.addEventListener("click", (evt) => {
        if (evt.target === overlay) {
            closePopup();
        }
    });
    document.addEventListener("keydown", (evt) => {
        if (evt.key === "Escape" && overlay.classList.contains("open")) {
            closePopup();
        }
    });

    function fallbackCopy() {
        const range = document.createRange();
        range.selectNodeContents(emailText);

        const selection = window.getSelection();
        selection.removeAllRanges();
        selection.addRange(range);
        try {
            const successful = document.execCommand("copy");
            selection.removeAllRanges();
            return successful;
        } catch (err) {
            selection.removeAllRanges();
            return false;
        }
    }

    copyBtn.addEventListener("click", () => {
        const clipboardWrite = navigator.clipboard && navigator.clipboard.writeText
            ? navigator.clipboard.writeText(EMAIL_ADDRESS)
            : Promise.reject(new Error("clipboard unavailable"));

        clipboardWrite.then(() => {
            copyBtn.textContent = "Copied!";
            copyBtn.disabled = true;
            setTimeout(() => {
                copyBtn.textContent = "Copy";
                copyBtn.disabled = false;
            }, 1500);
        }).catch(() => {
            if (fallbackCopy()) {
                copyBtn.textContent = "Copied!";
                copyBtn.disabled = true;
                setTimeout(() => {
                    copyBtn.textContent = "Copy";
                    copyBtn.disabled = false;
                }, 1500);
            } else {
                copyBtn.textContent = "Copy failed";
                setTimeout(() => {
                    copyBtn.textContent = "Copy";
                    copyBtn.disabled = false;
                }, 1500);
            }
        });
    });
})();
