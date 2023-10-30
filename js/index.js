const titleScreen = document.getElementById('titleScreen')
const cadetActionsSelect = document.getElementById('cadetActions')
const startButton = document.getElementById('startButton')
const goBackButton = document.getElementById('goBackButton')

startButton.onclick = () => {
	titleScreen.style.display = 'none'
	cadetActionsSelect.style.display = 'block'
}

goBackButton.onclick = () => {
	titleScreen.style.display = 'block'
	cadetActionsSelect.style.display = 'none'
}