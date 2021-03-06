! function(e) {
    var t = {};

    function n(i) {
        if (t[i]) return t[i].exports;
        var s = t[i] = {
            i: i,
            l: !1,
            exports: {}
        };
        return e[i].call(s.exports, s, s.exports, n), s.l = !0, s.exports
    }
    n.m = e, n.c = t, n.d = function(e, t, i) {
        n.o(e, t) || Object.defineProperty(e, t, {
            enumerable: !0,
            get: i
        })
    }, n.r = function(e) {
        "undefined" != typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
            value: "Module"
        }), Object.defineProperty(e, "__esModule", {
            value: !0
        })
    }, n.t = function(e, t) {
        if (1 & t && (e = n(e)), 8 & t) return e;
        if (4 & t && "object" == typeof e && e && e.__esModule) return e;
        var i = Object.create(null);
        if (n.r(i), Object.defineProperty(i, "default", {
                enumerable: !0,
                value: e
            }), 2 & t && "string" != typeof e)
            for (var s in e) n.d(i, s, function(t) {
                return e[t]
            }.bind(null, s));
        return i
    }, n.n = function(e) {
        var t = e && e.__esModule ? function() {
            return e.default
        } : function() {
            return e
        };
        return n.d(t, "a", t), t
    }, n.o = function(e, t) {
        return Object.prototype.hasOwnProperty.call(e, t)
    }, n.p = "", n(n.s = 0)
}([function(e, t, n) {
    "use strict";
    n.r(t);
    n(1);
    const i = /^(?!.*(__|--|_-|-_|\s).*)[^\W_][\w\-\s]+[^\W_]$/;
    t.default = class {
        constructor(e) {
            this.el = e, this.input = e.querySelector('input[type="hidden"]'), this.editable = e.querySelector("span[contenteditable]"), e.addEventListener("click", () => this.editable.focus()), this.editable.addEventListener("focus", () => e.classList.add("is-focused")), this.editable.addEventListener("blur", () => e.classList.remove("is-focused")), this.editable.addEventListener("keydown", this.onKeyDown.bind(this)), this.editable.addEventListener("paste", e => {
                e.preventDefault();
                const t = e.clipboardData.getData("text/plain"),
                    n = document.createElement("div");
                n.innerHTML = t, document.execCommand("insertHTML", !1, n.textContent.trim())
            }), this.input.value.split(",").filter(e => e.length > 0).forEach(e => this.addTag(e))
        }
        validateTag(e, t) {
            if (e.length > 2 && e.length <= 30 && -1 === t.indexOf(e) && i.test(e)) return !0
        }
        removeTag(e) {
            const t = this.input.value.split(","),
                n = Array.from(this.el.children).indexOf(e);
            t.splice(n, 1), this.input.value = t.join(","), this.el.removeChild(e)
        }
        addTag(e) {
            const t = document.createElement("div");
            t.className = "control", t.innerHTML = '<div class="tags has-addons">\n      <span class="tag is-success">'.concat(e, '</span>\n      <a class="tag is-delete"></a>\n    </div>'), t.querySelector(".is-delete").addEventListener("click", this.removeTag.bind(this, t));
            const n = this.el.children[this.el.children.length - 1];
            this.el.insertBefore(t, n)
        }
        onKeyDown(e) {
            if (["Enter", " ", ","].indexOf(e.key) >= 0) {
                e.preventDefault();
                const t = this.editable.textContent.trim(),
                    n = this.input.value.split(",").filter(e => e.length > 0);
                if (!this.validateTag(t, n)) return;
                n.push(t), this.input.value = n.join(","), this.addTag(t), this.editable.innerHTML = ""
            } else if ("Backspace" === e.key && 0 === this.editable.textContent.length && this.el.children.length > 1) {
                const e = this.el.children.length - 2,
                    t = this.el.children[e];
                this.removeTag(t)
            }
        }
    }
}, function(e, t, n) {}]);