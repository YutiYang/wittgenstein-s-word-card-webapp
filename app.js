// 1. "DOMContentLoaded" Vibe Check
// 确保 HTML 骨架加载完毕后，再运行我们的 JS 代码
document.addEventListener('DOMContentLoaded', () => {

    // 2. "抓取" 页面上的 Vibe 元素
    // 我们需要操作的 HTML 元素，都先用 "变量" 存起来
    const modelSelect = document.querySelector('select'); // 抓取下拉菜单
    const wordInput = document.querySelector('input[type="text"]'); // 抓取输入框
    const generateButton = document.querySelector('button'); // 抓取“生成”按钮
    const cardContainer = document.getElementById('card-container'); // 抓取卡片容器
    const cardBlueprint = document.getElementById('card-blueprint'); // 抓取 Day 2 "写死" 的卡片

    // 3. "默认隐藏" Vibe
    // 按照大纲要求，Day 2 的卡片只是个“蓝图”，默认不显示
    if (cardBlueprint) {
        cardBlueprint.style.display = 'none';
    }

    // 4. "点击 Vibe" - 给“生成”按钮添加事件监听
    generateButton.addEventListener('click', () => {
        
        // 5. "获取输入" Vibe
        // 当按钮被点击时，获取用户选择的模型和输入的单词
        const selectedModel = modelSelect.value;
        const inputWord = wordInput.value;

        // 6. "控制台 Vibe" - 在 "后台" 打印出来，检查一下
        console.log('所选模型:', selectedModel);
        console.log('输入单词:', inputWord);

        // 7. "隐藏蓝图" Vibe
        // 再次确保 Day 2 的卡片是隐藏的
        if (cardBlueprint) {
            cardBlueprint.style.display = 'none';
        }

        // 8. "加载 Vibe" - 显示“加载中...”动画
        // 这就是 Day 3 的核心产出！
        // 我们用 "innerHTML" 的方式，动态地塞一段 HTML 进去
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

        // (Day 6 我们会在这里 "fetch" 后端 API...)
    });

});