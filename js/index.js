	const titleScreen = document.getElementById('titleScreen');
    const goBackButton = document.getElementById('goBackButton');

	const cadetStartButton = document.getElementById('cadetStartButton');
	const cadetRegistration = document.getElementById('cadetRegistration');
	const cadetDataUpload = document.getElementById('cadetDataUpload');
	const cadetDisplay = document.getElementById('cadetDisplay');

	const seniorActions = document.getElementById('seniorActions');
	const seniorRegistration = document.getElementById('seniorRegistration');
	const seniorDataUpload = document.getElementById('seniorDataUpload');
	const seniorDisplay = document.getElementById('seniorDisplay');

	

	cadetStartButton.addEventListener('click', function () {
        titleScreen.style.display = 'none';
        cadetActions.style.display = 'block';
		seniorActions.style.display = 'block';

    });

	goBackButton.addEventListener('click', function () {
        titleScreen.style.display = 'block';
        cadetActions.style.display = 'none';
    });
	

	