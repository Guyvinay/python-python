import { Component, OnInit } from '@angular/core';
import { ChatService } from '../services/chat.service';

@Component({
  selector: 'app-chat-container',
  templateUrl: './chat-container.component.html',
  styleUrls: ['./chat-container.component.css']
})
export class ChatContainerComponent implements OnInit {
  
  ngOnInit(): void {
    
  }
  messages: { sender: string, content: string }[] = [];
  userInput = '';

  constructor(private chatService: ChatService) { }

  sendMessage(): void {
    if (this.userInput.trim() !== '') {
      // Add user message to the chat messages
      this.messages.push({ sender: 'User', content: this.userInput });

      // Send user message to the backend
      this.chatService.sendMessage(this.userInput).subscribe(
        (chatbotResponse) => {
        // Add chatbot response to the chat messages
        console.log(this.messages);
        
        this.messages.push({ sender: 'Chatbot', content: chatbotResponse });
        // this.messages.push(...chatbotResponse.map((message: any) => ({ sender: 'Chatbot', content: message })));
      },
      (error)=>{
        console.log(error);
      });

      // Clear user input after sending
      this.userInput = '';
    }
  }
}
