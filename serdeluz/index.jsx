import React, { useRef, useState } from 'react';
import emailjs from '@emailjs/browser';
import './styles.css';

export const ContactUs = () => {
  const form = useRef();
  const [status, setStatus] = useState(null);

  const sendEmail = (e) => {
    e.preventDefault();

    emailjs
      .sendForm('service_y9iayev', 'template_3glndmj', form.current, {
        publicKey: 'saTt1aqyAlTstrYk1',
      })
      .then(
        () => {
          setStatus('success');
          form.current.reset();
          setTimeout(() => setStatus(null), 5000);
        },
        (error) => {
          console.error('FAILED...', error.text);
          setStatus('error');
          setTimeout(() => setStatus(null), 5000);
        }
      );
  };

  return (
    <div className="contact-container">
      <h2 className="contact-title">Entre em Contato</h2>
      <p className="contact-description">Nos envie suas dúvidas, sugestões ou mensagens!</p>

      {status === 'success' && <p className="message success">✅ E-mail enviado com sucesso!</p>}
      {status === 'error' && <p className="message error">❌ Erro ao enviar. Tente novamente.</p>}

      <form ref={form} onSubmit={sendEmail} className="rd-form">
        <div className="form-wrap">
          <label className="form-label">Nome</label>
          <input type="text" name="user_name" className="form-input" required />
        </div>
        <div className="form-wrap">
          <label className="form-label">Email</label>
          <input type="email" name="user_email" className="form-input" required />
        </div>
        <div className="form-wrap">
          <label className="form-label">Mensagem</label>
          <textarea name="message" className="form-input" required />
        </div>
        <button type="submit" className="button-primary">Enviar</button>
      </form>
    </div>
  );
};
