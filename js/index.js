	const titleScreen = document.getElementById('titleScreen');
    const cadetActions = document.getElementById('cadetActions');
    const startButton = document.getElementById('startButton');
    const goBackButton = document.getElementById('goBackButton');


	startButton.addEventListener('click', function () {
        titleScreen.style.display = 'none';
        cadetActions.style.display = 'block';
    });

    goBackButton.addEventListener('click', function () {
        cadetActions.style.display = 'none';
        titleScreen.style.display = 'block';
    });