// 1. "DOMContentLoaded" Vibe Check (不变)
document.addEventListener('DOMContentLoaded', () => {

    // 2. "抓取" Vibe 元素 (不变)
    const modelSelect = document.querySelector('select');
    const wordInput = document.querySelector('input[type="text"]');
    const generateButton = document.querySelector('button');
    const cardContainer = document.getElementById('card-container');
    const cardBlueprint = document.getElementById('card-blueprint'); 

    // 3. "默认隐藏" Vibe (不变)
    if (cardBlueprint) {
        cardBlueprint.style.display = 'none';
    }

    // 4. "点击 Vibe" (Vibe 6.0 Async 版, 不变)
    generateButton.addEventListener('click', async () => {
        
        // 5. "获取输入" Vibe (不变)
        const selectedModel = modelSelect.value;
        const inputWord = wordInput.value;
        
        if (!inputWord) {
            alert("Vibe Check: 请 Vibe 输入一个单词！");
            return;
        }

        // 6. "控制台 Vibe" (不变)
        console.log('Vibe 6.0: 发起制卡请求...');
        console.log('所选模型 (前端 Vibe 名):', selectedModel);
        console.log('输入单词:', inputWord);

        // 7. "加载 Vibe" (不变)
        if (cardBlueprint) {
            cardBlueprint.style.display = 'none';
        }
        cardContainer.innerHTML = `
            <div class="bg-white rounded-lg shadow-xl overflow-hidden animate-pulse">
                <div class="p-6">
                    <div class="h-8 bg-gray-300 rounded w-1/2 mb-4"></div>
                    <div class="h-4 bg-gray-200 rounded w-3/4 mb-6"></div>
                    <div class="space-y-4">
                        <div class="h-4 bg-gray-200 rounded w-full"></div>
                        <div class="h-4 bg-gray-200 rounded w-5/6"></div>
                    </div>
                </div>
            </div>
        `;

        // 8. 【Vibe 6.0 核心: "Vibe 握手"】 (不变)
        try {
            const response = await fetch('http://127.0.0.1:8000/generate-card', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    word: inputWord,
                    model: selectedModel
                })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || "Vibe 6.0 后端 Vibe 握手失败");
            }

            // 9. 【Vibe 6.0 灵魂接收】(不变)
            const cardData = await response.json(); // (Vibe 6.0 "精简版" JSON 灵魂)
            console.log("Vibe 6.0: 成功接收到 JSON 灵魂！", cardData);

            // 10. 【Vibe 6.0 合体】(【Vibe 7.0 升级: Vibe 取消注释！】)
            // Vibe "Vibe 渲染"！
            renderCard(cardData); // Vibe 7.0: Vibe 开启 Vibe 渲染！

        } catch (error) {
            // (Vibe 错误处理, 不变)
            console.error("Vibe 6.0 握手 Vibe 失败:", error);
            cardContainer.innerHTML = `
                <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded-lg shadow-xl">
                    <strong class="font-bold">Vibe 6.0 握手失败!</strong>
                    <span class="block sm:inline">${error.message}</span>
                </div>
            `;
        }
    });

    // 11. 【Vibe 6.0 核心: The "Vibe 渲染器"】(【Vibe 7.0 升级: Vibe 填充灵魂！】)
    // Vibe Vibe 接收 Vibe 6.0 JSON 灵魂 (data)
    // Vibe Vibe "拼装" Day 2 "Vibe 蓝图"
    function renderCard(data) {
        console.log("Vibe 7.0: 'renderCard' Vibe 被调用，Vibe 准备 Vibe 渲染...", data);

        // Vibe 7.0 A: Vibe "动态拼装" Vibe 6.0 的 "language_games" (Vibe 2.0 的)
        // Vibe (这是一个 Vibe "map-join" Vibe 骚操作)
        const gamesHTML = data.language_games.map(game => `
            <div>
                <h3 class="text-lg font-semibold text-gray-800 mb-1">
                    [${game.context}] </h3>
                <p class="text-gray-700 italic">
                    "${game.sentence}" </p>
            </div>
        `).join(''); // Vibe Vibe "join" 成一个 Vibe "大字符串"

        // Vibe 7.0 B: Vibe "动态拼装" Vibe 6.0 的 "collocations"
        const collocationsHTML = data.collocations.map(collocation => `
            <li class="bg-gray-100 p-2 rounded-md text-gray-700">${collocation}</li>
        `).join('');

        // Vibe 7.0 C: Vibe "拼装" Vibe 最终的 Vibe "高颜值" HTML 
        const cardHTML = `
            <div class="bg-white rounded-lg shadow-xl overflow-hidden animate-fadeIn"> <div class="p-8">
                    
                    <div class="mb-6">
                        <h2 class="text-5xl font-bold text-gray-900 mb-2">
                            ${data.word} </h2>
                        <p class="text-xl text-gray-600">
                            ${data.core_game} </p>
                    </div>

                    <div class="space-y-5">
                        ${gamesHTML} </div>

                    <div class="mt-8 pt-6 border-t border-gray-200">
                        <h4 class="text-sm font-bold text-blue-600 mb-3">
                            Vibe 词块 (Collocations)
                        </h4>
                        <ul class="flex flex-wrap gap-2">
                            ${collocationsHTML} </ul>
                    </div>

                    <div class="mt-8 pt-6 border-t border-gray-200">
                        <h4 class="text-sm font-bold text-blue-600 mb-2">
                            哲学家提示 (Vibe Tip)
                        </h4>
                        <p class="text-gray-700">
                            ${data.mnemonic_tip} </p>
                    </div>

                </div>
            </div>
            `;

        // Vibe 7.0 D: Vibe "Duang"！ 替换 Vibe "加载动画"
        cardContainer.innerHTML = cardHTML;

        // Vibe 7.0 E (Vibe 可选): Vibe 添加一个 Vibe "fadeIn" 动画
        // Vibe (我们 Vibe 6.0 的 Vibe 蓝图 Vibe 6.0 `tailwind.config.js` Vibe 不支持 Vibe 自定义 Vibe 动画,
        // Vibe 但 Vibe 6.0 的 Vibe Tailwind CDN Vibe 3.0 Vibe 支持 Vibe "animate-fadeIn")
        // Vibe (我在 Vibe C 步 `class="..."` 里 Vibe 加上了 `animate-fadeIn`)
    }
});