// Функция для выбора инструмента "Risk/Reward Short" (SELL)
async function selectRiskRewardShort() {
    console.log("📌 Выбираю инструмент 'Risk/Reward Short' (SELL)...");

    const sellButton = document.querySelector("[data-name='FavoriteToolbarLineToolRiskRewardShort']");
    if (!sellButton) {
        console.error("❌ Кнопка 'Risk/Reward Short' не найдена!");
        return;
    }

    sellButton.click();
    console.log("✅ Инструмент 'Risk/Reward Short' выбран!");

    await new Promise(r => setTimeout(r, 1000)); // Ожидаем активации инструмента
}

// Функция для установки точки SELL на графике
async function placeSellOrder() {
    console.log("🖱 Щелкаю на графике для установки SELL...");

    // Находим область графика (ищем основной контейнер графика)
    const chartArea = document.querySelector(".chart-container, .chart-content, .layout__area--center");

    if (!chartArea) {
        console.error("❌ График не найден!");
        return;
    } else {
        console.log(`chartArea:  ${chartArea}`)
    }

    // Кликаем на центр графика
    const rect = chartArea.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;

    chartArea.dispatchEvent(new MouseEvent("click", { bubbles: true, clientX: centerX, clientY: centerY }));
    console.log("✅ Точка SELL установлена!");

    await new Promise(r => setTimeout(r, 1000)); // Ждем появления точки
}

// Функция для двойного клика по SELL точке
async function doubleClickSellPoint() {
    console.log("🖱 Дважды щелкаю для редактирования...");

    // Кликаем туда же, где ставили SELL
    const chartArea = document.querySelector(".chart-container, .chart-content, .layout__area--center");

    if (!chartArea) {
        console.error("❌ График не найден!");
        return;
    }

    const rect = chartArea.getBoundingClientRect();
    const centerX = rect.left + rect.width / 2;
    const centerY = rect.top + rect.height / 2;

    chartArea.dispatchEvent(new MouseEvent("dblclick", { bubbles: true, clientX: centerX, clientY: centerY }));
    console.log("✅ Меню редактирования открыто!");

    await new Promise(r => setTimeout(r, 1500)); // Ждем появления поля редактирования
}

// Функция для ввода цены и подтверждения
async function enterSellPrice(price = "1.792") {

    const priceInput = document.querySelector("input[data-property-id='Risk/RewardshortEntryPrice']");
    if (!priceInput) {
        console.error("❌ Поле ввода цены не найдено! Проверяю снова...");
        await new Promise(r => setTimeout(r, 1000)); // Пробуем еще раз через секунду
    }

    // Повторная попытка поиска
    const retryPriceInput = document.querySelector("input[data-property-id='Risk/RewardshortEntryPrice']");
    if (!retryPriceInput) {
        console.error("❌ Поле ввода цены не появилось!");
        return;
    }

    retryPriceInput.value = price;
    retryPriceInput.dispatchEvent(new Event("input", { bubbles: true }));

    await new Promise(r => setTimeout(r, 500));

    // Подтверждение выбора
    const okButton = document.querySelector("button[data-name='submit-button']");
    if (!okButton) {
        console.error("❌ Кнопка 'Ок' не найдена!");
        return;
    }

    okButton.click();
    console.log("✅ Цена установлена и подтверждена!");
}

// Основная функция выполнения действий
async function executeSellOrder() {
    setTimeout(await selectRiskRewardShort, 1000)  // Выбираем инструмент
    setTimeout(await placeSellOrder, 1000)         // Щелкаем на графике
    setTimeout(await doubleClickSellPoint, 1000)   // Двойной клик по точке
    setTimeout(await enterSellPrice, 1000)         // Вводим цену и подтверждаем
}

// Запуск процесса
setTimeout(executeSellOrder, 1000)