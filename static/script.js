document.addEventListener("DOMContentLoaded", function () {

    const generateBtn = document.getElementById("generateBtn");
    const resultImage = document.getElementById("resultImage");
    const placeholder = document.getElementById("placeholder");
    const downloadBtn = document.getElementById("downloadBtn");

    const designType = document.getElementById("designType");

    const logoFields = document.getElementById("logoFields");
    const posterFields = document.getElementById("posterFields");
    const bannerFields = document.getElementById("bannerFields");

    // Show / Hide dynamic fields
    designType.addEventListener("change", function () {
        logoFields.classList.add("hidden");
        posterFields.classList.add("hidden");
        bannerFields.classList.add("hidden");

        if (designType.value === "logo") {
            logoFields.classList.remove("hidden");
        } else if (designType.value === "poster") {
            posterFields.classList.remove("hidden");
        } else if (designType.value === "banner") {
            bannerFields.classList.remove("hidden");
        }
    });

    generateBtn.addEventListener("click", async function () {

        const type = designType.value;
        const brandName = document.getElementById("nameInput").value;
        const industry = document.getElementById("industryInput").value;
        const style = document.getElementById("styleInput").value;
        const theme = document.getElementById("themeInput").value;

        let main_text = "";
        let sub_text = "";

        if (type === "logo") {
            main_text = brandName;
            sub_text = document.getElementById("logoSlogan").value;
        } else if (type === "poster") {
            main_text = document.getElementById("posterHeading").value;
            sub_text = document.getElementById("posterTagline").value;
        } else if (type === "banner") {
            main_text = document.getElementById("bannerHeadline").value;
            sub_text = document.getElementById("bannerText").value;
        }

        const response = await fetch("/generate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                type: type,
                main_text: main_text,
                sub_text: sub_text,
                color_style: style,
                tagline: theme
            })
        });

        const data = await response.json();

        resultImage.src = data.image_url + "?t=" + new Date().getTime();
        resultImage.style.display = "block";
        placeholder.style.display = "none";

        downloadBtn.href = data.image_url;
        downloadBtn.style.opacity = "1";
        downloadBtn.style.pointerEvents = "auto";
        downloadBtn.textContent = "Download Design";
    });

});