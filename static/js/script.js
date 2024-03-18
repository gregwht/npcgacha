// var imageContainer = document.querySelector('.image-container');
var imageContainer = document.getElementById('image-container');
var overlayText = document.getElementById('overlay-text');
var refreshIcon = document.getElementById('refresh-icon');


// SELECT ALL / DESELECT ALL CHECKBOXES BUTTONS
// General Attributes checkboxes
var buttonResetAttributes = document.getElementById('button-reset-attributes')
buttonResetAttributes.addEventListener('click', resetAttributes)
var attributesSelected = true;

function resetAttributes() {

    if (attributesSelected === true) {
        document.getElementById('checkbox-first-initial').checked = false;
        document.getElementById('checkbox-last-initial').checked = false;
        document.getElementById('checkbox-alignment').checked = false;
        document.getElementById('checkbox-race').checked = false;
        document.getElementById('checkbox-class').checked = false;
        attributesSelected = false;
        buttonResetAttributes.innerText = 'Select All';
    }
    else {
        document.getElementById('checkbox-first-initial').checked = true;
        document.getElementById('checkbox-last-initial').checked = true;
        document.getElementById('checkbox-alignment').checked = true;
        document.getElementById('checkbox-race').checked = true;
        document.getElementById('checkbox-class').checked = true;
        attributesSelected = true;
        buttonResetAttributes.innerText = 'Deselect All';
    }
}

// Race checkboxes
var buttonResetRaces = document.getElementById('button-reset-races')
buttonResetRaces.addEventListener('click', resetRaces)
var racesSelected = true;

function resetRaces() {

    if (racesSelected === true) {
        document.getElementById('checkbox-race-Dragonborn').checked = false;
        document.getElementById('checkbox-race-Dwarf').checked = false;
        document.getElementById('checkbox-race-Elf').checked = false;
        document.getElementById('checkbox-race-Gnome').checked = false;
        document.getElementById('checkbox-race-Half-Elf').checked = false;
        document.getElementById('checkbox-race-Halfling').checked = false;
        document.getElementById('checkbox-race-Half-Orc').checked = false;
        document.getElementById('checkbox-race-Human').checked = false;
        document.getElementById('checkbox-race-Tiefling').checked = false;
        racesSelected = false;
        buttonResetRaces.innerText = 'Select All';
    }
    else {
        document.getElementById('checkbox-race-Dragonborn').checked = true;
        document.getElementById('checkbox-race-Dwarf').checked = true;
        document.getElementById('checkbox-race-Elf').checked = true;
        document.getElementById('checkbox-race-Gnome').checked = true;
        document.getElementById('checkbox-race-Half-Elf').checked = true;
        document.getElementById('checkbox-race-Halfling').checked = true;
        document.getElementById('checkbox-race-Half-Orc').checked = true;
        document.getElementById('checkbox-race-Human').checked = true;
        document.getElementById('checkbox-race-Tiefling').checked = true;
        racesSelected = true;
        buttonResetRaces.innerText = 'Deselect All';
    }
}

// Class checkboxes
var buttonResetClasses = document.getElementById('button-reset-classes')
buttonResetClasses.addEventListener('click', resetClasses)
var classesSelected = true;

function resetClasses() {

    if (classesSelected === true) {
        document.getElementById('checkbox-class-Barbarian').checked = false;
        document.getElementById('checkbox-class-Bard').checked = false;
        document.getElementById('checkbox-class-Cleric').checked = false;
        document.getElementById('checkbox-class-Druid').checked = false;
        document.getElementById('checkbox-class-Fighter').checked = false;
        document.getElementById('checkbox-class-Monk').checked = false;
        document.getElementById('checkbox-class-Paladin').checked = false;
        document.getElementById('checkbox-class-Ranger').checked = false;
        document.getElementById('checkbox-class-Rogue').checked = false;
        document.getElementById('checkbox-class-Sorcerer').checked = false;
        document.getElementById('checkbox-class-Warlock').checked = false;
        document.getElementById('checkbox-class-Wizard').checked = false;
        classesSelected = false;
        buttonResetClasses.innerText = 'Select All';
    }
    else {
        document.getElementById('checkbox-class-Barbarian').checked = true;
        document.getElementById('checkbox-class-Bard').checked = true;
        document.getElementById('checkbox-class-Cleric').checked = true;
        document.getElementById('checkbox-class-Druid').checked = true;
        document.getElementById('checkbox-class-Fighter').checked = true;
        document.getElementById('checkbox-class-Monk').checked = true;
        document.getElementById('checkbox-class-Paladin').checked = true;
        document.getElementById('checkbox-class-Ranger').checked = true;
        document.getElementById('checkbox-class-Rogue').checked = true;
        document.getElementById('checkbox-class-Sorcerer').checked = true;
        document.getElementById('checkbox-class-Warlock').checked = true;
        document.getElementById('checkbox-class-Wizard').checked = true;
        classesSelected = true;
        buttonResetClasses.innerText = 'Deselect All';
    }
}


// GENERATE CHARACTER BUTTON
var buttonGenerateCharacter = document.getElementById('button-generate-character');
buttonGenerateCharacter.addEventListener('click', sendSettings);
var imageCapsule = document.getElementById('img-capsule'); 
var imageGpt = document.getElementById('img-gpt')

function sendSettings() {

    // Get checkbox states: Attributes
    var firstInitialChecked = document.getElementById('checkbox-first-initial').checked;
    var lastInitialChecked = document.getElementById('checkbox-last-initial').checked;
    var alignmentChecked = document.getElementById('checkbox-alignment').checked;
    var raceChecked = document.getElementById('checkbox-race').checked;
    var classChecked = document.getElementById('checkbox-class').checked;
    
    // Get checkbox states: Races
    var checkedRaces = [];
    document.querySelectorAll('input[name^="checkbox-race-"]:checked').forEach(function(checkbox) {
        // Find the associated label
        var label = checkbox.closest('label');
        // Ensure that the found element is indeed a label e.g. 'Dwarf'
        if (label) {
            // The text content includes the race name, but might also include whitespace or other characters due to the checkmark span, so trim it
            var raceText = label.textContent.trim() || label.innerText.trim();
            // Exclude the checkmark span text if present
            // This might need adjustment based on the actual text content and structure within the label
            var raceName = raceText.replace("checkmark", "").trim();
            // Add the cleaned-up race name to the list of checked races
            checkedRaces.push(raceName);
        }
    });
    console.log("Checked races:", checkedRaces);
    // Handle no checked races
    if (checkedRaces.length === 0) {
        checkedRaces.push("None")
    }

    // Get checkbox states: Classes
    var checkedClasses = [];
    document.querySelectorAll('input[name^="checkbox-class-"]:checked').forEach(function(checkbox) {
        // Find the associated label
        var label = checkbox.closest('label');
        // Ensure that the found element is indeed a label e.g. 'Barbarian'
        if (label) {
            // The text content includes the race name, but might also include whitespace or other characters due to the checkmark span, so trim it
            var classText = label.textContent.trim() || label.innerText.trim();
            // Exclude the checkmark span text if present
            // This might need adjustment based on the actual text content and structure within the label
            var className = classText.replace("checkmark", "").trim();
            // Add the cleaned-up race name to the list of checked classes
            checkedClasses.push(className);
        }
    });
    console.log("Checked classes:", checkedClasses);
    // Handle no checked classes
    if (checkedClasses.length === 0) {
        checkedClasses.push("None")
    }

    // Get GPT settings
    var gptNameChecked = document.getElementById('checkbox-gpt-name').checked;
    var genderSelected = document.getElementById('dropdown-gender').value;
    var genreSelected = document.getElementById('dropdown-genre').value;

    if (gptNameChecked) {
        buttonGenerateCharacter.disabled = true;
        buttonGenerateCharacter.style.backgroundColor = '#C2E1DD';
        buttonGenerateCharacter.style.color = 'black';
        buttonGenerateCharacter.textContent = "Generating Character...";
        imageCapsule.classList.add('rotate-on-click');
    }

    // Send AJAX request to Flask backend
    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            firstInitialChecked: firstInitialChecked,
            lastInitialChecked: lastInitialChecked,
            alignmentChecked: alignmentChecked,
            raceChecked: raceChecked,
            classChecked: classChecked,

            checkedRaces: checkedRaces,
            checkedClasses: checkedClasses,
            
            gptNameChecked: gptNameChecked,
            genreSelected: genreSelected,
            genderSelected: genderSelected
        })
    })
    .then(response => response.json())
    .then(data => {
        // Update the webpage with the generated values
        document.getElementById('input-first-name').value = data.first_name;
        document.getElementById('input-last-name').value = data.last_name;
        document.getElementById('input-alignment').value = data.alignment;
        document.getElementById('input-race').value = data.race;
        document.getElementById('input-class').value = data.class;

        buttonGenerateCharacter.disabled = false;
        buttonGenerateCharacter.style.backgroundColor = '';
        buttonGenerateCharacter.style.color = '';
        buttonGenerateCharacter.textContent = "Generate Character";
        imageCapsule.classList.remove('rotate-on-click');
        
    })
    .catch(error => {
        console.error('Error:', error);

        buttonGenerateCharacter.disabled = false;
        buttonGenerateCharacter.style.backgroundColor = '';
        buttonGenerateCharacter.style.color = '';
        buttonGenerateCharacter.textContent = "Generate Character";
        imageCapsule.classList.remove('rotate-on-click');
        overlayText.textContent = "An error has occurred: " + error;
        overlayText.style.opacity = '1';
    });
}


// REROLL ATTRIBUTES
function rerollAttribute(attributeName){
    
    console.log("Reroll attribute.");

    // Send AJAX request to Flask backend
    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'reroll-attribute': attributeName
        })
    })
    .then(response => response.json())
    .then(data => {
        // Update the webpage with the generated values
        document.getElementById('input-first-name').value = data.first_name;
        document.getElementById('input-last-name').value = data.last_name;
        document.getElementById('input-alignment').value = data.alignment;
        document.getElementById('input-race').value = data.race;
        document.getElementById('input-class').value = data.class;
    })
    .catch(error => {
        console.error('Error:', error);
    });

}


// SENDING USER-INPUTTED NAMES TO BACKEND
document.addEventListener("DOMContentLoaded", function(){

    const inputFirstName = document.getElementById("input-first-name");
    const inputLastName = document.getElementById("input-last-name");
    const inputAlignment = document.getElementById("input-alignment");
    let originalFirstName = inputFirstName.value;
    let originalLastName = inputLastName.value;
    let originalAlignment = inputAlignment.value;

    // When the input field gains focus, store the current value 
    inputFirstName.addEventListener('focus', function(){ 
        originalFirstName = inputFirstName.value;
    })
    inputLastName.addEventListener('focus', function(){ 
        originalLastName = inputLastName.value;
    })
    inputAlignment.addEventListener('focus', function(){
        originalAlignment = inputAlignment.value;
    })

    // When focus is lost, check if the value has changed
    inputFirstName.addEventListener('blur', function() {
        // If the value has changed, send the data
        if (inputFirstName.value !== originalFirstName) {
            sendFirstName(inputFirstName.value);
        }
    })
    inputLastName.addEventListener('blur', function() {
        // If the value has changed, send the data
        if (inputLastName.value !== originalLastName) {
            sendLastName(inputLastName.value);
        }
    })
    inputAlignment.addEventListener('blur', function(){
        // If the value has changed, send the data
        if (inputAlignment.value !== originalAlignment) {
            sendAlignment(inputAlignment.value);
        }
    })

    // If Enter key is pressed, check if the value has changed
    inputFirstName.addEventListener('keypress', function(event) {
        if (event.key === 'Enter' && inputFirstName.value !== originalFirstName) {
            event.preventDefault(); // Prevent the default action to avoid form submission or other unwanted behaviour
            sendFirstName(inputFirstName.value);
        }
    })
    inputFirstName.addEventListener('keypress', function(event) {
        if (event.key === 'Enter' && inputLastName.value !== originalLastName) {
            event.preventDefault(); // Prevent the default action to avoid form submission or other unwanted behaviour
            sendLastName(inputLastName.value);
        }
    })
    inputAlignment.addEventListener('keypress', function(event) {
        if (event.key === 'Enter' && inputAlignment.value !== originalAlignment) {
            event.preventDefault(); // Prevent the default action to avoid form submission or other unwanted behaviour
            sendAlignment(inputAlignment.value);
        }
    })


    // Sending new values to backend
    function sendFirstName(name) {

        console.log("Sending data:", name); // Placeholder for AJAX call

        fetch('/save-attribute/first-name', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ inputFirstName: name }),
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch((error) => {
            console.error('Error:', error);
        })
    }

    function sendLastName(name) {

        console.log("Sending data:", name); // Placeholder for AJAX call

        fetch('/save-attribute/last-name', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ inputLastName: name }),
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch((error) => {
            console.error('Error:', error);
        })
    }

    function sendAlignment(alignment) {

        console.log("Sending data:", alignment); // Placeholder for AJAX call

        fetch('/save-attribute/alignment', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ inputAlignment: alignment }),
        })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch((error) => {
            console.error('Error:', error);
        })
    }
})


// GENERATE PORTRAIT IMAGE
imageCapsule.addEventListener('click', generateImage);
imageGpt.addEventListener('click', generateImage);

function generateImage() {
    
    // Get information needed for image generation
    var genreSelected = document.getElementById('dropdown-genre').value;
    var genderSelected = document.getElementById('dropdown-gender').value;
    var firstName = document.getElementById('input-first-name').value;
    var lastName = document.getElementById('input-last-name').value;
    var alignment = document.getElementById('input-alignment').value;
    var race = document.getElementById('input-race').value;
    var class_ = document.getElementById('input-class').value;

    console.log('genreSelected:', genreSelected);
    console.log('genderSelected:', genderSelected);
    console.log('firstName:', firstName);
    console.log('lastName:', lastName);
    console.log('alignment:', alignment);
    console.log('race:', race);
    console.log('class_:', class_);

    // Stop listening for clicks on the images
    imageCapsule.removeEventListener('click', generateImage);
    imageCapsule.style.cursor = 'default';
    imageGpt.removeEventListener('click', generateImage);
    imageGpt.style.cursor = 'default';
        
    // Alter Generate Character button appearance
    buttonGenerateCharacter.disabled = true;
    buttonGenerateCharacter.style.backgroundColor = '#C2E1DD';
    buttonGenerateCharacter.style.color = 'black';
    buttonGenerateCharacter.textContent = "Generating Portrait...";
    
    // Hide current GPT image if one exists
   imageGpt.style.display = 'none';
    // Show gachapon capsule image
    imageCapsule.style.display = 'inline-block';
    // Spin gachapon capsule image
    imageCapsule.classList.add('rotate-on-click');
    // Hide overlay text
    imageContainer.classList.add('disabled');


    fetch('/generate-image', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'genre': genreSelected,
            'gender': genderSelected,
            'firstName': firstName,
            'lastName': lastName,
            'alignment': alignment,
            'race': race,
            'class': class_
        }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        // Return Generate Character button appearance to normal
        buttonGenerateCharacter.disabled = false;
        buttonGenerateCharacter.style.backgroundColor = '';
        buttonGenerateCharacter.style.color = '';
        buttonGenerateCharacter.textContent = "Generate Character";

        // Replace src attribute of image to Dall-E result
        imageGpt.src = data.imageUrl;
        // Hide the gachapon capsule and stop it spinning
        imageCapsule.style.display = 'none';
        imageCapsule.classList.remove('rotate-on-click');
        // Display the GPT image
        imageGpt.style.display = 'inline-block';
        // Change overlay text
        imageContainer.classList.remove('disabled');
        overlayText.textContent = "Click to open image in a new tab";

        // Listen for clicks on the images again
        imageCapsule.style.cursor = '';
        imageGpt.style.cursor = '';
        imageGpt.addEventListener('click', function() {
            // Clicking on image opens it in new window
            window.open(this.src, '_blank');
        });

        // Enable hovering over the image reveals refresh icon
        imageContainer.classList.add('icon-active');
        // Hovering over refresh icon changes overlay text
        var originalText = overlayText.textContent;
        refreshIcon.addEventListener('mouseenter', function(){
            overlayText.textContent = "Click to generate new portrait";
        });
        refreshIcon.addEventListener('mouseleave', function(){
            overlayText.textContent = originalText;
        });
        // Clicking on refresh icon...
        refreshIcon.addEventListener('click', function(){
            // ...generates new image...
            generateImage();
            // ...and disables refresh icon again
            imageContainer.classList.remove('icon-active');
        });
        
    })
    .catch((error) => {
        console.error('Error:', error);
        // Handle errors here
        // Return Generate Character button appearance to normal
        buttonGenerateCharacter.disabled = false;
        buttonGenerateCharacter.style.backgroundColor = '';
        buttonGenerateCharacter.style.color = '';
        buttonGenerateCharacter.textContent = "Generate Character";

        // Replace src attribute of image to placeholder
        imageGpt.src = 'static/img/placeholder.jpg';
        // Hide the gachapon capsule and stop it spinning
        imageCapsule.style.display = 'none';
        imageCapsule.classList.remove('rotate-on-click');
        // Display the placeholder image
        imageGpt.style.display = 'inline-block';
        // Change overlay text
        // imageContainer.classList.remove('disabled');
        overlayText.textContent = "An error has occurred: " + error;
        overlayText.style.opacity = '1';
        

        // Listen for clicks on the images again
        imageCapsule.addEventListener('click', generateImage);
        imageCapsule.style.cursor = '';
        imageGpt.addEventListener('click', generateImage);
        imageGpt.style.cursor = '';
    });
}
