import unittest

# ---------- 任务1：计算列表最大嵌套深度 ----------
def max_depth(lst):
    """
    返回列表的最大嵌套深度。
    最外层列表深度记为 1，空列表深度也为 1。
    如果传入的不是列表，返回 0（但题目保证传入列表）。
    """
    if not isinstance(lst, list):
        return 0
    if not lst:          # 空列表，深度为 1
        return 1
    # 非空列表：1 + 所有元素中最大的深度（元素为非列表时深度为 0）
    return 1 + max(max_depth(item) for item in lst)


# ---------- 任务2：单元测试（至少5个用例） ----------
class TestMaxDepth(unittest.TestCase):
    def test_flat_list(self):
        """普通一维列表，深度应为1"""
        self.assertEqual(max_depth([1, 2, 3]), 1)

    def test_empty_list(self):
        """空列表，深度应为1"""
        self.assertEqual(max_depth([]), 1)

    def test_nested_depth_3(self):
        """嵌套深度为3的列表"""
        self.assertEqual(max_depth([[1], [2, [3]]]), 3)

    def test_deeper_nesting(self):
        """深度为4的列表"""
        self.assertEqual(max_depth([1, [2, [3, [4]]]]), 4)

    def test_only_nested_empty(self):
        """仅包含空列表的列表，深度为2"""
        self.assertEqual(max_depth([[]]), 2)

    def test_multiple_branches(self):
        """不同分支深度不同，应取最大值"""
        self.assertEqual(max_depth([1, [2, [3]], [[[4]]]]), 4)

    def test_non_list_element(self):
        """元素包含非列表类型，不影响深度计算"""
        self.assertEqual(max_depth([1, 'a', [2]]), 2)


if __name__ == '__main__':
    unittest.main()