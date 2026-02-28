document.addEventListener("DOMContentLoaded", () => {

    const typeSelect = document.getElementById("designType");
    const industryInput = document.getElementById("industryInput");
    const styleInput = document.getElementById("styleInput");
    const themeInput = document.getElementById("themeInput");

    const generateBtn = document.getElementById("generateBtn");
    const resultImage = document.getElementById("resultImage");
    const placeholder = document.getElementById("placeholder");
    const downloadBtn = document.getElementById("downloadBtn");
    // Dynamic Fields
const logoFields = document.getElementById("logoFields");
const posterFields = document.getElementById("posterFields");
const bannerFields = document.getElementById("bannerFields");

function hideAllFields() {
    logoFields.classList.add("hidden");
    posterFields.classList.add("hidden");
    bannerFields.classList.add("hidden");
}

typeSelect.addEventListener("change", function () {
    hideAllFields();

    if (this.value === "logo") {
        logoFields.classList.remove("hidden");
    }

    if (this.value === "poster") {
        posterFields.classList.remove("hidden");
    }

    if (this.value === "banner") {
        bannerFields.classList.remove("hidden");
    }
});

// Show correct fields on page load
typeSelect.dispatchEvent(new Event("change"));

    generateBtn.addEventListener("click", generateDesign);

    async function generateDesign() {

        const type = typeSelect.value;
        let name = "";

if (type === "logo") {
    name = document.getElementById("logoSlogan").value.trim();
}

if (type === "poster") {
    name = document.getElementById("posterHeading").value.trim();
}

if (type === "banner") {
    name = document.getElementById("bannerHeadline").value.trim();
}
        const industry = industryInput.value.trim();
        const style = styleInput.value.trim();
        const theme = themeInput.value.trim();

        if (!name) {
            alert("Please enter name!");
            return;
        }

        generateBtn.disabled = true;
        generateBtn.innerText = "Generating...";

        try {
            const response = await fetch("/generate", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    type: type,
                    name: name,
                    industry: industry,
                    style: style,
                    theme: theme
                })
            });

            const data = await response.json();

            if (data.error) {
                alert(data.message);
                return;
            }

            resultImage.src = data.image;
            placeholder.classList.add("hidden");
            resultImage.classList.remove("hidden");
downloadBtn.href = data.image;
downloadBtn.download = "design.png";
downloadBtn.style.opacity = "1";
downloadBtn.style.pointerEvents = "auto";

        } catch (error) {
            alert("Server error. Check backend.");
        }

        generateBtn.disabled = false;
        generateBtn.innerText = "Generate Design";
    }

});