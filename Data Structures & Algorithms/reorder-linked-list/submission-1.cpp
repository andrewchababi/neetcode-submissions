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
    void reorderList(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head->next;

        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode* secondHead = slow->next;
        ListNode* prev = slow->next = nullptr;

        while (secondHead != nullptr) {
            ListNode* temp = secondHead->next;
            secondHead->next = prev;
            prev = secondHead;
            secondHead = temp;
        }

        ListNode* first = head;
        secondHead = prev;
        while (secondHead != nullptr) {
            ListNode* temp1 = first->next;
            ListNode* temp2 = secondHead->next;
            first->next = secondHead;
            secondHead->next = temp1;
            first = temp1;
            secondHead = temp2;
        }
    }
};
