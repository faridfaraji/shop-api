from awesoon.core.shopify.query import ShopifyQuery

query_platforms = {
    "shopify": {
        "querier": ShopifyQuery,
        "queries": [
            ShopifyQuery.get_shop_categories,
            ShopifyQuery.get_shop_policies,
            ShopifyQuery.get_shop_products,
            ShopifyQuery.get_shop_pages,
            ShopifyQuery.get_shop_articles,
            ShopifyQuery.get_shop_orders,
        ]
    }
}
