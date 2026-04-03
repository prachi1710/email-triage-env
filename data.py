import random

emails = [

# ================= EASY (10) =================

{
 "email": {"subject": "Refund request", "email_text": "I want a refund for my recent order", "sender": "user1@gmail.com", "task_type": "easy"},
 "ground_truth": {"category": "support", "priority": "medium", "action": "reply", "response": "We will process your refund shortly."}
},
{
 "email": {"subject": "Order status", "email_text": "Can you tell me where my order is?", "sender": "user2@gmail.com", "task_type": "easy"},
 "ground_truth": {"category": "support", "priority": "medium", "action": "reply", "response": "Your order status will be shared shortly."}
},
{
 "email": {"subject": "Discount offer", "email_text": "Check out our new deals and discounts!", "sender": "promo@shop.com", "task_type": "easy"},
 "ground_truth": {"category": "sales", "priority": "low", "action": "archive", "response": "Promotional email archived."}
},
{
 "email": {"subject": "Meeting reminder", "email_text": "Reminder for our meeting tomorrow at 10 AM", "sender": "boss@company.com", "task_type": "easy"},
 "ground_truth": {"category": "personal", "priority": "medium", "action": "reply", "response": "Acknowledged the meeting reminder."}
},
{
 "email": {"subject": "Spam offer", "email_text": "You won a lottery! Click here!", "sender": "spam@fake.com", "task_type": "easy"},
 "ground_truth": {"category": "spam", "priority": "low", "action": "ignore", "response": "Spam email ignored."}
},
{
 "email": {"subject": "Password reset", "email_text": "Click here to reset your password", "sender": "no-reply@service.com", "task_type": "easy"},
 "ground_truth": {"category": "personal", "priority": "medium", "action": "archive", "response": "Password reset email archived."}
},
{
 "email": {"subject": "Order delivered", "email_text": "Your order has been delivered successfully", "sender": "store@shop.com", "task_type": "easy"},
 "ground_truth": {"category": "support", "priority": "low", "action": "archive", "response": "Delivery confirmation noted."}
},
{
 "email": {"subject": "Subscription renewal", "email_text": "Your subscription will renew soon", "sender": "service@company.com", "task_type": "easy"},
 "ground_truth": {"category": "sales", "priority": "low", "action": "archive", "response": "Subscription notice archived."}
},
{
 "email": {"subject": "Job application", "email_text": "I am applying for the open position", "sender": "candidate@gmail.com", "task_type": "easy"},
 "ground_truth": {"category": "personal", "priority": "medium", "action": "reply", "response": "Thank you for your application."}
},
{
 "email": {"subject": "Invoice attached", "email_text": "Please find the invoice attached", "sender": "finance@company.com", "task_type": "easy"},
 "ground_truth": {"category": "personal", "priority": "medium", "action": "archive", "response": "Invoice received and archived."}
},

# ================= MEDIUM (10) =================

{
 "email": {"subject": "Order delay", "email_text": "My order hasn't arrived and I need it soon", "sender": "user3@gmail.com", "task_type": "medium"},
 "ground_truth": {"category": "support", "priority": "high", "action": "escalate", "response": "We are escalating your issue for faster resolution."}
},
{
 "email": {"subject": "Late delivery", "email_text": "This is taking too long, where is my package?", "sender": "user4@gmail.com", "task_type": "medium"},
 "ground_truth": {"category": "support", "priority": "high", "action": "escalate", "response": "We apologize and are prioritizing your request."}
},
{
 "email": {"subject": "Promo mail", "email_text": "Limited time sale, grab now!", "sender": "ads@shop.com", "task_type": "medium"},
 "ground_truth": {"category": "sales", "priority": "low", "action": "archive", "response": "Promotional email archived."}
},
{
 "email": {"subject": "Complaint", "email_text": "The product quality is not good", "sender": "user5@gmail.com", "task_type": "medium"},
 "ground_truth": {"category": "support", "priority": "medium", "action": "reply", "response": "We are sorry for the inconvenience."}
},
{
 "email": {"subject": "Account issue", "email_text": "I cannot log into my account", "sender": "user6@gmail.com", "task_type": "medium"},
 "ground_truth": {"category": "support", "priority": "high", "action": "escalate", "response": "We are looking into your login issue."}
},
{
 "email": {"subject": "Newsletter", "email_text": "Our weekly newsletter is here", "sender": "news@company.com", "task_type": "medium"},
 "ground_truth": {"category": "sales", "priority": "low", "action": "archive", "response": "Newsletter archived."}
},
{
 "email": {"subject": "Urgent help", "email_text": "Need help with my order ASAP", "sender": "user7@gmail.com", "task_type": "medium"},
 "ground_truth": {"category": "support", "priority": "high", "action": "escalate", "response": "We are prioritizing your request."}
},
{
 "email": {"subject": "Feedback", "email_text": "Your service was good but can improve", "sender": "user8@gmail.com", "task_type": "medium"},
 "ground_truth": {"category": "personal", "priority": "low", "action": "archive", "response": "Thank you for your feedback."}
},
{
 "email": {"subject": "Payment issue", "email_text": "Payment failed but money deducted", "sender": "user9@gmail.com", "task_type": "medium"},
 "ground_truth": {"category": "support", "priority": "high", "action": "escalate", "response": "We are resolving your payment issue."}
},
{
 "email": {"subject": "Offer inside", "email_text": "Exclusive deal just for you", "sender": "offers@shop.com", "task_type": "medium"},
 "ground_truth": {"category": "sales", "priority": "low", "action": "archive", "response": "Promotional email archived."}
},

# ================= HARD (10) =================

{
 "email": {"subject": "???", "email_text": "hey ordered last wk… no update 😕 need asap", "sender": "user10@gmail.com", "task_type": "hard"},
 "ground_truth": {"category": "support", "priority": "high", "action": "escalate", "response": "We understand and are prioritizing your order."}
},
{
 "email": {"subject": "", "email_text": "money gone but no order?? fix this", "sender": "user11@gmail.com", "task_type": "hard"},
 "ground_truth": {"category": "support", "priority": "high", "action": "escalate", "response": "We are urgently investigating your issue."}
},
{
 "email": {"subject": "help", "email_text": "cant login again n again error", "sender": "user12@gmail.com", "task_type": "hard"},
 "ground_truth": {"category": "support", "priority": "high", "action": "escalate", "response": "We are resolving your login problem."}
},
{
 "email": {"subject": "offer??", "email_text": "is this real or scam??", "sender": "user13@gmail.com", "task_type": "hard"},
 "ground_truth": {"category": "spam", "priority": "low", "action": "ignore", "response": "This appears to be a suspicious email."}
},
{
 "email": {"subject": "late", "email_text": "package still not here… disappointed", "sender": "user14@gmail.com", "task_type": "hard"},
 "ground_truth": {"category": "support", "priority": "high", "action": "escalate", "response": "We apologize and are expediting your order."}
},
{
 "email": {"subject": "??", "email_text": "need it tmrw otherwise cancel", "sender": "user15@gmail.com", "task_type": "hard"},
 "ground_truth": {"category": "support", "priority": "high", "action": "escalate", "response": "We are prioritizing your request immediately."}
},
{
 "email": {"subject": "", "email_text": "why charged twice???", "sender": "user16@gmail.com", "task_type": "hard"},
 "ground_truth": {"category": "support", "priority": "high", "action": "escalate", "response": "We are investigating the double charge."}
},
{
 "email": {"subject": "???", "email_text": "weird mail saying i won something lol", "sender": "user17@gmail.com", "task_type": "hard"},
 "ground_truth": {"category": "spam", "priority": "low", "action": "ignore", "response": "This is likely a spam email."}
},
{
 "email": {"subject": "broken", "email_text": "item came broken not happy", "sender": "user18@gmail.com", "task_type": "hard"},
 "ground_truth": {"category": "support", "priority": "high", "action": "escalate", "response": "We are sorry and will resolve this quickly."}
},
{
 "email": {"subject": "", "email_text": "order?? idk whats happening anymore", "sender": "user19@gmail.com", "task_type": "hard"},
 "ground_truth": {"category": "support", "priority": "high", "action": "escalate", "response": "We are looking into your order issue."}
},
# ================= MORE EASY (10) =================

{
 "email": {"subject": "Thanks", "email_text": "Thank you for your help", "sender": "user20@gmail.com", "task_type": "easy"},
 "ground_truth": {"category": "personal", "priority": "low", "action": "archive", "response": "Acknowledged."}
},
{
 "email": {"subject": "Newsletter", "email_text": "This week’s updates and news", "sender": "news@company.com", "task_type": "easy"},
 "ground_truth": {"category": "sales", "priority": "low", "action": "archive", "response": "Newsletter archived."}
},
{
 "email": {"subject": "Login alert", "email_text": "New login detected on your account", "sender": "security@service.com", "task_type": "easy"},
 "ground_truth": {"category": "personal", "priority": "high", "action": "archive", "response": "Security alert noted."}
},
{
 "email": {"subject": "Promotion", "email_text": "Big sale this weekend!", "sender": "ads@shop.com", "task_type": "easy"},
 "ground_truth": {"category": "sales", "priority": "low", "action": "archive", "response": "Promotional email archived."}
},
{
 "email": {"subject": "Delivery update", "email_text": "Your package is out for delivery", "sender": "delivery@shop.com", "task_type": "easy"},
 "ground_truth": {"category": "support", "priority": "medium", "action": "archive", "response": "Delivery update noted."}
},
{
 "email": {"subject": "Spam link", "email_text": "Earn money fast click now", "sender": "fake@spam.com", "task_type": "easy"},
 "ground_truth": {"category": "spam", "priority": "low", "action": "ignore", "response": "Spam ignored."}
},
{
 "email": {"subject": "Reminder", "email_text": "Don’t forget your appointment tomorrow", "sender": "clinic@health.com", "task_type": "easy"},
 "ground_truth": {"category": "personal", "priority": "medium", "action": "archive", "response": "Reminder acknowledged."}
},
{
 "email": {"subject": "Welcome", "email_text": "Welcome to our platform!", "sender": "team@company.com", "task_type": "easy"},
 "ground_truth": {"category": "sales", "priority": "low", "action": "archive", "response": "Welcome email archived."}
},
{
 "email": {"subject": "OTP", "email_text": "Your OTP is 123456", "sender": "no-reply@bank.com", "task_type": "easy"},
 "ground_truth": {"category": "personal", "priority": "high", "action": "archive", "response": "OTP noted."}
},
{
 "email": {"subject": "Ad campaign", "email_text": "Check our latest campaign", "sender": "ads@brand.com", "task_type": "easy"},
 "ground_truth": {"category": "sales", "priority": "low", "action": "archive", "response": "Promotional email archived."}
},

# ================= MORE MEDIUM (10) =================

{
 "email": {"subject": "Refund delayed", "email_text": "My refund has not been processed yet", "sender": "user21@gmail.com", "task_type": "medium"},
 "ground_truth": {"category": "support", "priority": "high", "action": "reply", "response": "We are checking your refund status."}
},
{
 "email": {"subject": "Wrong item", "email_text": "Received a different item than ordered", "sender": "user22@gmail.com", "task_type": "medium"},
 "ground_truth": {"category": "support", "priority": "high", "action": "reply", "response": "We will resolve your issue shortly."}
},
{
 "email": {"subject": "Cancel order", "email_text": "I want to cancel my order", "sender": "user23@gmail.com", "task_type": "medium"},
 "ground_truth": {"category": "support", "priority": "medium", "action": "reply", "response": "Your cancellation request is received."}
},
{
 "email": {"subject": "Pricing inquiry", "email_text": "Can you share pricing details?", "sender": "client@business.com", "task_type": "medium"},
 "ground_truth": {"category": "sales", "priority": "medium", "action": "reply", "response": "Sharing pricing details."}
},
{
 "email": {"subject": "Account blocked", "email_text": "My account got blocked suddenly", "sender": "user24@gmail.com", "task_type": "medium"},
 "ground_truth": {"category": "support", "priority": "high", "action": "reply", "response": "We will assist you in resolving this."}
},
{
 "email": {"subject": "Discount request", "email_text": "Can I get a discount on bulk order?", "sender": "buyer@shop.com", "task_type": "medium"},
 "ground_truth": {"category": "sales", "priority": "medium", "action": "reply", "response": "We will check available offers."}
},
{
 "email": {"subject": "Feedback", "email_text": "Your service is good but slow", "sender": "user25@gmail.com", "task_type": "medium"},
 "ground_truth": {"category": "support", "priority": "medium", "action": "reply", "response": "Thanks for your feedback."}
},
{
 "email": {"subject": "Invoice missing", "email_text": "I did not receive the invoice", "sender": "user26@gmail.com", "task_type": "medium"},
 "ground_truth": {"category": "support", "priority": "medium", "action": "reply", "response": "We will resend the invoice."}
},
{
 "email": {"subject": "Meeting reschedule", "email_text": "Can we reschedule our meeting?", "sender": "colleague@company.com", "task_type": "medium"},
 "ground_truth": {"category": "personal", "priority": "medium", "action": "reply", "response": "Sure, let's reschedule."}
},
{
 "email": {"subject": "Trial expired", "email_text": "Your trial period has ended", "sender": "service@company.com", "task_type": "medium"},
 "ground_truth": {"category": "sales", "priority": "low", "action": "archive", "response": "Trial notification archived."}
},

# ================= MORE HARD (10) =================

{
 "email": {"subject": "???", "email_text": "got charged twice?? fix asap", "sender": "user27@gmail.com", "task_type": "hard"},
 "ground_truth": {"category": "support", "priority": "high", "action": "reply", "response": "We are checking your double charge issue."}
},
{
 "email": {"subject": "help", "email_text": "cant login tried everything", "sender": "user28@gmail.com", "task_type": "hard"},
 "ground_truth": {"category": "support", "priority": "high", "action": "reply", "response": "We will help you recover your account."}
},
{
 "email": {"subject": "offer??", "email_text": "this looks fake or real??", "sender": "user29@gmail.com", "task_type": "hard"},
 "ground_truth": {"category": "spam", "priority": "medium", "action": "reply", "response": "This may be a scam. Avoid sharing details."}
},
{
 "email": {"subject": "late", "email_text": "package still not here", "sender": "user30@gmail.com", "task_type": "hard"},
 "ground_truth": {"category": "support", "priority": "high", "action": "reply", "response": "We will check your delivery status."}
},
{
 "email": {"subject": "???", "email_text": "need invoice urgently for taxes", "sender": "user31@gmail.com", "task_type": "hard"},
 "ground_truth": {"category": "support", "priority": "high", "action": "reply", "response": "We will send your invoice soon."}
},
{
 "email": {"subject": "refund??", "email_text": "where is my money??", "sender": "user32@gmail.com", "task_type": "hard"},
 "ground_truth": {"category": "support", "priority": "high", "action": "reply", "response": "We are checking your refund."}
},
{
 "email": {"subject": "broken item", "email_text": "product arrived damaged", "sender": "user33@gmail.com", "task_type": "hard"},
 "ground_truth": {"category": "support", "priority": "high", "action": "reply", "response": "We will resolve this issue."}
},
{
 "email": {"subject": "scam??", "email_text": "got suspicious mail asking for OTP", "sender": "user34@gmail.com", "task_type": "hard"},
 "ground_truth": {"category": "spam", "priority": "high", "action": "reply", "response": "This is likely phishing. Do not share OTP."}
},
{
 "email": {"subject": "delay", "email_text": "order delayed again not happy", "sender": "user35@gmail.com", "task_type": "hard"},
 "ground_truth": {"category": "support", "priority": "high", "action": "reply", "response": "We apologize and are checking your order."}
},
{
 "email": {"subject": "??", "email_text": "subscription auto charged again why", "sender": "user36@gmail.com", "task_type": "hard"},
 "ground_truth": {"category": "support", "priority": "medium", "action": "reply", "response": "We will review your subscription charges."}
}

]

def get_email(task_type):
    filtered = [e for e in emails if e["email"]["task_type"] == task_type]
    sample = random.choice(filtered)
    return sample["email"], sample["ground_truth"]

def get_sample():
    sample = random.choice(emails)
    return sample["email"], sample["ground_truth"]