# 语音对话模型评测平台

一个用于展示和比较语音对话模型性能的现代化网页平台。

## 功能特性

- 📊 **排行榜展示**: 支持多语言（中英文）模型性能对比
- 🎵 **样本展示**: 分类展示不同模型的音频样本和评分
- 🔄 **交互式界面**: 支持排序、筛选和语言切换
- 📱 **响应式设计**: 适配桌面端和移动端
- 🚀 **GitHub Pages**: 支持直接部署到GitHub Pages

## 项目结构

```
├── index.html          # 主页面
├── styles.css          # 样式文件
├── script.js           # JavaScript逻辑
├── data/              # 数据文件夹
│   ├── leaderboard.json # 排行榜数据
│   ├── samples.json    # 样本数据
│   └── samples/        # 音频文件存储
│       ├── en/         # 英文样本
│       │   ├── phonological/
│       │   ├── semantic/
│       │   ├── ambiguity/
│       │   ├── omission/
│       │   ├── coreference/
│       │   ├── multiturn/
│       │   └── context/
│       └── zh/         # 中文样本
│           ├── phonological/
│           ├── semantic/
│           ├── ambiguity/
│           ├── omission/
│           ├── coreference/
│           ├── multiturn/
│           └── context/
└── README.md           # 项目说明
```

## 数据格式

### 排行榜数据 (data/leaderboard.json)

```json
{
  "english": [
    {
      "rank": 1,
      "model": "模型名称",
      "link": "模型链接",
      "phonological": 53.45,
      "semantic": 70.59,
      "ambiguity": 62.02,
      "omission": 16.18,
      "coreference": 91.11,
      "multiturn": 47.06,
      "context": 51.45,
      "overall": 55.68
    }
  ],
  "chinese": [...]
}
```

### 样本数据 (data/samples.json)

```json
{
  "en": {
    "phonological": [
      {
        "id": "phon_en_001",
        "title": "样本标题",
        "description": "样本描述",
        "instruction_audio": "音频文件路径",
        "instruction_text": "指令文本",
        "responses": [
          {
            "model": "模型名称",
            "audio": "回复音频路径",
            "text": "回复文本",
            "gemini_score": 9.2,
            "score_label": "excellent"
          }
        ]
      }
    ]
  }
}
```

## 部署到GitHub Pages

1. Fork或克隆此仓库
2. 将您的数据文件放入相应目录
3. 在GitHub仓库设置中启用Pages功能
4. 选择主分支作为源
5. 访问生成的GitHub Pages URL

## 更新数据

### 更新排行榜数据

1. 编辑 `data/leaderboard.json`
2. 按照现有格式更新模型数据
3. 确保包含所有必要的评测指标

### 更新样本数据

1. 将音频文件放入对应的类别文件夹
2. 编辑 `data/samples.json`
3. 更新样本条目，包含音频路径和文本

## 技术栈

- **前端**: 纯HTML、CSS、JavaScript
- **样式**: CSS Grid、Flexbox、CSS变量
- **图标**: Lucide Icons
- **字体**: Inter字体
- **部署**: GitHub Pages

## 浏览器兼容性

- Chrome 88+
- Firefox 85+
- Safari 14+
- Edge 88+



## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 联系方式

如有问题或建议，请联系项目维护者。
