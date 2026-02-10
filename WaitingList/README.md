# Podspec 批量替换工具使用说明

## 功能说明

批量替换当前目录下所有 `.podspec` 文件中的占位符。

## 配置项

在 `batch_replace_podspec.py` 文件中修改以下配置：

### 1. VERSION_PLACEHOLDER_REPLACEMENT
- **说明**: 要发的 adapter 版本名称
- **替换**: `(version_placeholder)` → 配置的值
- **示例**: `"6.4.93"`

### 2. PREFIX_PLACEHOLDER_REPLACEMENT
- **说明**: adapter 前缀，`AnyThink` 或 `TPN`
- **替换**: `(prefix_placeholder)` → 配置的值
- **特殊行为**: 如果配置为 `TPN`，会将文件名中的 `AnyThink` 也替换为 `TPN`
- **示例**: 
  - 配置 `"TPN"` 
  - 文件 `AnyThinkMediationGromoreAdapter.podspec` → `TPNMediationGromoreAdapter.podspec`

### 3. PERSONALIZE_PLACEHOLDER_REPLACEMENT
- **说明**: 个性化标识，默认直接移除（不替换为其他字符串）
- **替换**: `(personalize_placeholder)` → 配置的值
- **示例**: `""` (空字符串，表示移除)

### 4. VERSION_VARIABLE_REPLACEMENT
- **说明**: 当前 OSS 上的 adapter 版本号
- **替换**: `#{s.version}` → 配置的值
- **示例**: `"7.4.0.0"`

### 5. CORE_VERSION_PLACEHOLDER_REPLACEMENT
- **说明**: Core SDK 版本号
- **替换**: `(core_version_placeholder)` → 配置的值
- **示例**: `"v6.4.94"` (默认值)

### 6. HOMEPAGE_REPLACEMENT
- **说明**: Pod 项目主页 URL
- **替换**: `s.homepage` 整行的值
- **示例**: `"https://github.com/toponteam/AnyThinkPrivateSDK"` (默认值)

## 使用方法

### 步骤 1：配置参数

编辑 `batch_replace_podspec.py` 文件，修改配置区域：

```python
# ==================== 配置区域 ====================

VERSION_PLACEHOLDER_REPLACEMENT = "6.4.93"
PREFIX_PLACEHOLDER_REPLACEMENT = "TPN"
PERSONALIZE_PLACEHOLDER_REPLACEMENT = ""
VERSION_VARIABLE_REPLACEMENT = "7.4.0.0"
CORE_VERSION_PLACEHOLDER_REPLACEMENT = "v6.4.94"
HOMEPAGE_REPLACEMENT = "https://github.com/toponteam/AnyThinkPrivateSDK"

# ==================== 配置结束 ====================
```

### 步骤 2：运行脚本

在 WaitingList 目录下执行：

```bash
python3 batch_replace_podspec.py
```

### 步骤 3：查看结果

脚本会输出处理结果，包括：
- 找到的 podspec 文件数量
- 每个文件的处理状态
- 成功替换的文件数量
- 重命名的文件数量

## 示例

### 配置示例

```python
VERSION_PLACEHOLDER_REPLACEMENT = "6.4.93"
PREFIX_PLACEHOLDER_REPLACEMENT = "TPN"
PERSONALIZE_PLACEHOLDER_REPLACEMENT = ""
VERSION_VARIABLE_REPLACEMENT = "7.4.0.0"
CORE_VERSION_PLACEHOLDER_REPLACEMENT = "v6.4.94"
HOMEPAGE_REPLACEMENT = "https://github.com/toponteam/AnyThinkPrivateSDK"
```

### 替换效果

**原始内容:**
```ruby
Pod::Spec.new do |s|
  s.name = '(prefix_placeholder)MediationGromoreAdapter(personalize_placeholder)'
  s.version = '(version_placeholder)'
  s.source = {
    :http => "https://...AnyThinkGromoreAdapter/#{s.version}/..."
  }
  s.dependency 'Ads-CN-Beta/BUAdSDK', '7.4.0.0'
end
```

**替换后:**
```ruby
Pod::Spec.new do |s|
  s.name = 'TPNMediationGromoreAdapter'
  s.version = '6.4.93'
  s.homepage = 'https://github.com/toponteam/AnyThinkPrivateSDK'
  s.source = {
    :http => "https://...AnyThinkGromoreAdapter/7.4.0.0/..."
  }
  s.dependency 'Ads-CN-Beta/BUAdSDK', '7.4.0.0'
end
```

**文件名:**
- `AnyThinkMediationGromoreAdapter.podspec` → `TPNMediationGromoreAdapter.podspec`

## 注意事项

1. ⚠️ **备份**: 建议先备份原文件，脚本会直接修改文件
2. ✅ **编码**: 脚本使用 UTF-8 编码处理文件
3. 🔍 **检查**: 运行后请检查替换结果是否符合预期
4. 📁 **目录**: 脚本只处理与脚本同目录下的 `.podspec` 文件

## 常见问题

### Q: 如何只替换部分文件？
A: 可以将其他文件临时移到别的目录，或修改脚本中的文件查找逻辑。

### Q: 替换后发现错误怎么办？
A: 从 git 恢复原文件，修改配置后重新运行。

### Q: 如何保持 AnyThink 前缀？
A: 将 `PREFIX_PLACEHOLDER_REPLACEMENT` 配置为 `"AnyThink"`

### Q: #{s.version} 在文件中有多处，都会替换吗？
A: 是的，所有匹配的地方都会被替换。
