def crawl_price(product: str) -> str:
    """
    模拟爬取三大平台价格（实际项目中替换为真实爬虫）
    """
    # 简单关键词匹配（实际可用模糊搜索）
    if "iphone" in product.lower() or "苹果" in product:
        return (
            "京东: ¥5999 (销量12,000+, 好评率98%) | "
            "淘宝: ¥5899 (销量8,500+, 好评率96%) | "
            "拼多多: ¥5699 (销量5,200+, 好评率94%)"
        )
    elif "耳机" in product:
        return "京东: ¥199 | 淘宝: ¥189 | 拼多多: ¥159"
    else:
        return "未找到该商品，请尝试更具体的名称（如'iPhone 15'）"