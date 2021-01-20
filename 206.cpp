/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode*cur = head;
        ListNode*prev = nullptr;
        ListNode*temp = nullptr;
        while (cur) {
            temp = cur;
            cur = cur->next;
            temp->next = prev;
            prev = temp;
        }
        return prev;

    }
};