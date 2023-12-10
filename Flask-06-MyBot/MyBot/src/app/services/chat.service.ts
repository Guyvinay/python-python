import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class ChatService {


  private apiUrl = 'http://localhost:5000'; // Update with your backend API URL

  constructor(private http: HttpClient) { }

  sendMessage(message: string): Observable<string> {
    const body = { message };
    return this.http.post<string>(`${this.apiUrl}/send-message`, body);
  }
}
